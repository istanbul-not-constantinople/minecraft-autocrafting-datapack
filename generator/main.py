import os 
import shutil
import json
import wx
from datetime import datetime as time
import numpy as np
import sys
import re
def simp_pack_path(path):
  return re.sub(r'\s+','_',path)
def simp_nmsp_path(path):
  return 'ac.g.' + re.sub(r'\.ac\.g$', '', re.sub(r'(\s+|-)','_',path))
def verify_pack_root(path):
  tpath = os.path.abspath(path)
  if not os.path.exists(tpath):
    os.makedirs(tpath)
  if not os.path.isdir(os.path.join(tpath, 'data','ac','tags','functions','api')):
    os.makedirs(os.path.join(tpath, 'data','ac','tags','functions','api'))
  if not os.path.isdir(os.path.join(tpath, 'data','minecraft','tags','functions')):
    os.makedirs(os.path.join(tpath, 'data','minecraft','tags','functions'))
  space = simp_nmsp_path(os.path.basename(os.path.normpath(path)))
  nmsp = os.path.join(tpath, 'data', space)
  if not os.path.isdir(os.path.join(nmsp,'functions')):
    os.makedirs(os.path.join(nmsp,'functions'))
  if not os.path.isdir(os.path.join(nmsp,'tags','items')):
    os.makedirs(os.path.join(nmsp,'tags','items'))
  if not os.path.isdir(os.path.join(nmsp,'predicates')):
    os.makedirs(os.path.join(nmsp,'predicates'))
  if not os.path.isfile(os.path.join(tpath, 'pack.mcmeta')):
    with open(os.path.join(tpath, 'pack.mcmeta'),'w+') as f:
      f.write('{"pack":{"pack_format":6,"description":"generated recipepack for radiish\'s autocrafting datapack"}}')
  if not os.path.isfile(os.path.join(tpath, 'data', 'ac', 'tags', 'functions', 'api','craft.json')):
    with open(os.path.join(tpath, 'data', 'ac', 'tags', 'functions', 'api','craft.json'),'w+') as f:
      f.write(f'{{"replace":false,"values":["{space}:recipes"]}}')
  if not os.path.isfile(os.path.join(tpath, 'data', 'minecraft', 'tags', 'functions','load.json')):
    with open(os.path.join(tpath, 'data', 'minecraft', 'tags', 'functions','load.json'),'w+') as f:
      f.write(f'{{"replace":false,"values":["{space}:load"]}}')
  return '\\\\?\\' + tpath
def pack_nmsp(path):
  return os.path.join(os.path.abspath(path), 'data', simp_nmsp_path(os.path.basename(os.path.normpath(path))))
def mcpath(path):
  return path.replace('\\','/')
supress = False
slots = ['3','4','5','12','13','14','21','22','23']
not_table = ['smoking','stonecutting','smelting','blasting','campfire_cooking']

g_log = ""
g_gui = None
def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")

  return os.path.join(base_path, relative_path)
def log_print(msg):
  global g_gui
  g_gui.log.SetValue(g_gui.log.GetValue() + '\n' + msg)
  g_gui.Layout()

def clear_contents(path):
  shutil.rmtree(path)
  os.mkdir(path)

def nested_paths(dest, ignore = []):
  result = []
  listdir = os.listdir(dest)
  for f in listdir:
    if f in ignore:
      continue
    if os.path.isfile(os.path.join(dest, f)):
      result.append(os.path.join(dest, f))
    else:
      nest = nested_paths(os.path.join(dest, f))
      nest.extend(result)
      result = nest
  return result

class kitem:
  def __init__(self,value):
    self.value = value.split(':')[1]
    self.namespace = value.split(':')[0]
    self.both = value
    self.item = True
class ktag:
  def __init__(self,value):
    self.value = value.split(':')[1]
    self.namespace = value.split(':')[0]
    self.both = value
    self.item = False
def create_predicate(tag,root,tagname = None):
  if tagname == None:
    tagname = f'{tag.namespace}:{tag.value}'
  pathi = os.path.join(root,'predicates','tags',tag.namespace)
  if not os.path.isdir(pathi):
    os.makedirs(pathi)
  with open(os.path.join(pathi, tag.value) + '.json','w+') as f:
    f.write(f'{{"condition":"minecraft:entity_properties","entity":"this","predicate":{{"equipment":{{"feet":{{"tag":"{tagname}"}}}}}}}}')
def create_tag(options,root,namespace):
  item = kitem(options[0])
  pathi2 = os.path.join(root,'tags','items',item.namespace)
  if not os.path.isdir(pathi2):
    os.makedirs(pathi2)
  strops = ''
  for op in options:
    strops += f'"{op}"'
    if op != options[len(options)-1]:
      strops += ','
  with open(os.path.join(pathi2,item.value) + '.json','w+') as f:
    f.write(f'{{"replace":false,"values":[{strops}]}}')
  create_predicate(item,root,f'{namespace}:{item.namespace}/{item.value}')
def write_functions(keys_in,out_id,out_count,root,namespace):
  path = os.path.join(root,'functions','recipes')
  old_path = path
  if os.path.isfile(old_path + '.mcfunction') == False:
    open(old_path + '.mcfunction','w+').close()
  if os.path.isdir(path) == False:
    os.mkdir(path)
  for i in range(8):
    if i > 0:
      old_path = path
    path += '/' + keys_in[i].value
    func_path = 'recipes/' + '/'.join(path.split('/')[1:])
    if os.path.isdir('\\'.join(path.split('/'))) == False:
      os.mkdir('\\'.join(path.split('/')))
      open('\\'.join(path.split('/')) + '.mcfunction','w+').close()
      with open('\\'.join(old_path.split('/')) + '.mcfunction','a+') as file:
        file.write(f'#{keys_in[i].both}\n')
        if keys_in[i].item:
          if keys_in[i].both == 'builtin:null':
            file.write(f'execute unless data block ~ ~1 ~ {{Items:[{{Slot:{slots[i]}b}}]}} run function {namespace}:{func_path}\n')
          else:
            file.write(f'execute if data block ~ ~1 ~ {{Items:[{{Slot:{slots[i]}b,id:"{keys_in[i].both}"}}]}} run function {namespace}:{func_path}\n')
        else:
          file.write('data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}\n')
          file.write(f'data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{{Slot:{slots[i]}b}}].id\n')
          file.write(f'execute if predicate {namespace}:tags/{keys_in[i].namespace}/{keys_in[i].value} run function {namespace}:{func_path}\n')
  with open('\\'.join(path.split('/')) + '.mcfunction','a+') as file:
    file.write(f'#{keys_in[8].both}\n')
    if keys_in[8].item:
      if keys_in[8].both == 'builtin:null':
        file.write(f'execute unless data block ~ ~1 ~ {{Items:[{{Slot:{slots[8]}b}}]}} run function {namespace}:{func_path}/{keys_in[8].value}\n')
      else:
        file.write(f'execute if data block ~ ~1 ~ {{Items:[{{Slot:{slots[8]}b,id:"{keys_in[8].both}"}}]}} run function {namespace}:{func_path}/{keys_in[8].value}\n')
    else:
      file.write('data modify entity @s ArmorItems[0] set value {id:"minecraft:jigsaw",Count:1b}\n')
      file.write(f'data modify entity @s ArmorItems[0].id set from block ~ ~1 ~ Items[{{Slot:{slots[8]}b}}].id\n')
      file.write(f'execute if predicate {namespace}:tags/{keys_in[8].namespace}/{keys_in[8].value} run function {namespace}:{func_path}/{keys_in[8].value}\n')
  with open('\\'.join(path.split('/')) + '\\' + keys_in[8].value+'.mcfunction','w+') as file:
    file.write(f'data modify block ~ ~1 ~ Items[{{Slot:0b}}] set value {{Slot:0b,id:"{out_id}",Count:{out_count}b}}\n')
    file.write('tag @s add ac.offering\n')
    file.write('data modify entity @s ArmorItems[1].tag.ac_last set from block ~ ~1 ~ Items\n')
    for i in range(9):
      if keys_in[i].both == 'builtin:null':
        file.write(f'data modify entity @s ArmorItems[1].tag.ac_last append value {{Slot:{slots[i]}b,id:"minecraft:structure_void",Count:1b,tag:{{ac_gui:1b,CustomModelData:2b,display:{{Name:\'""\'}}}}}}\n')

def create_recipe(path,root,namespace):
  with open(path) as file:
    data = json.load(file)
    ctype = data['type'].split(':')[-1]
    if ctype == 'crafting_shaped':
      x = len(data['pattern'][0])
      y = len(data['pattern'])
      pattern = np.zeros((y,x))
      keys = [' ']
      key_values = [kitem('builtin:null')]
      for xi in range(x):
        for yi in range(y):
          key = data['pattern'][yi][xi]
          if key in keys:
            pattern[yi][xi] = keys.index(key)
          else:
            pattern[yi][xi] = len(keys)
            keys.append(key)
            if 'item' in data['key'][key]:
              key_values.append(kitem(data['key'][key]['item']))
            elif 'tag' in data['key'][key]:
              key_values.append(ktag(data['key'][key]['tag']))
            elif isinstance(data['key'][key],list):
              ops = []
              for i in data['key'][key]:
                if 'item' in i:
                  ops.append(i['item'])
                elif 'tag' in i:
                  ops.append('#' + i['tag'])
              create_tag(ops,root,namespace)
              key_values.append(ktag(ops[0]))
            else:
              key_values.append(kitem('builtin:null'))
      pattern = np.pad(pattern, ((0,3-y),(0,3-x)),mode='constant',constant_values=0)
      keys_in = []
      for yi in range(3):
        for xi in range(3):
          app = key_values[int(pattern[yi][xi])]
          keys_in.append(app)
      result_id = data['result']['item']
      if "count" in data['result']:
        result_count = data['result']['count']
      else:
        result_count = 1
      write_functions(keys_in,result_id,result_count,root,namespace)
      return True
    elif ctype == 'crafting_shapeless':
      result_id = data['result']['item']
      if 'count' in data['result']:
        result_count = data['result']['count']
      else:
        result_count = 1
      keys_in = []
      ingreds = data['ingredients']
      i = 0
      for i in range(len(ingreds)):
        if 'item' in ingreds[i]:
          keys_in.append(kitem(ingreds[i]['item']))
        elif 'tag' in ingreds[i]:
          keys_in.append(ktag(ingreds[i]['tag']))
        elif isinstance(ingreds[i],list):
          ops = []
          for i2 in ingreds[i]:
            if 'item' in i2:
              ops.append(i2['item'])
          create_tag(ops,root,namespace)
          op = f'{namespace}:' + ops[0][ops[0].index(':') + 1:]
          keys_in.append(ktag(op))
        else:
          keys_in.append(kitem('builtin:null'))
      for i2 in range(9-i):
        keys_in.append(kitem('builtin:null'))
      write_functions(keys_in,result_id,result_count,root,namespace)
      return True
    else:
      if not supress:
        if ctype == 'crafting_special':
          log_print(f'invalid recipe. unable to create recipe ({os.path.basename(path)}) because its features are not emulatable by the current system ({ctype})')
        elif ctype in not_table:
          log_print(f'invalid recipe. unable to create recipe ({os.path.basename(path)}) because it is implemented by other means ({ctype})')
        else:
          log_print(f'invalid recipe. unable to create recipe ({os.path.basename(path)}) beacuse of an incompatible crafting_type ({ctype})')
        return False
def create_from_dir(path,root,namespace):
  listdir = nested_paths(path)
  for f in listdir:
    if os.path.splitext(f)[1] == '.json':
      create_recipe(f,root,namespace)


class gui(wx.Frame):

  def __init__(self, *args, **kwargs):
    super(gui, self).__init__(*args, **kwargs)

    self.SetSize((560, 640))
    self.SetTitle('recipe generator')
    self.Centre()

    menubar = wx.MenuBar()
    fileMenu = wx.Menu()

    qmi = wx.MenuItem(fileMenu, wx.ID_CLOSE, '&quit\tCtrl+Q')
    fileMenu.Append(qmi)
    self.Bind(wx.EVT_MENU, self.quit, id=wx.ID_CLOSE)
    
    imi = wx.MenuItem(fileMenu, -1, '&import (source)\tCtrl+I')
    fileMenu.Append(imi)
    self.Bind(wx.EVT_MENU, self.onimport, imi)
    omi = wx.MenuItem(fileMenu, -1, '&open (destination)\tCtrl+O')
    fileMenu.Append(omi)
    self.Bind(wx.EVT_MENU, self.open, omi)
    
    rmi = wx.MenuItem(fileMenu, 3, '&reset all recipes')
    fileMenu.Append(rmi)
    self.Bind(wx.EVT_MENU, self.reset, id=3)

    menubar.Append(fileMenu, '&File')
    self.SetMenuBar(menubar)

    panel = wx.Panel(self)

    icon = wx.Icon()
    icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ICO))
    self.SetIcon(icon)

    wx.StaticText(panel, -1, label='source path:', pos=(20, 0), size=(500, 20))
    self.input = wx.TextCtrl(panel, -1, value='[path to your recipes datapack]', pos=(20, 20), size=(500, 40), style = wx.TE_MULTILINE)
  
    wx.StaticText(panel, -1, label='destination path:', pos=(20, 60), size=(500, 20))
    self.output = wx.TextCtrl(panel, -1, value='[path to your newly created datapack folder]', pos=(20, 80), size=(500, 40), style = wx.TE_MULTILINE)
  
    panel.Bind(wx.EVT_BUTTON, self.generate, wx.Button(panel, -1, label='generate reicpes', pos=(200,140), size=(160,40)))
  
    wx.StaticText(panel, -1, label='log:', pos=(20, 180), size=(500, 20))
    self.log = wx.TextCtrl(panel, -1, value=f'[generator opened at {time.now().strftime("%Y-%m-%d %H:%M:%S")}]', pos=(20, 200), size=(500, 260), style = wx.TE_MULTILINE | wx.TE_READONLY)
    
    self.Bind(wx.EVT_CLOSE, self.quit, self)
  def quit(self,e):
    log_print(f'[generator closed at {time.now().strftime("%Y-%m-%d %H:%M:%S")}]')
    with open('last.log','w+') as log:
      log.write(self.log.GetValue())
    self.Destroy()
  def onimport(self, e):
    with wx.DirDialog (None, "choose source directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
      if dirDialog.ShowModal() == wx.ID_CANCEL:
        return
      path = dirDialog.GetPath()
      self.input.SetValue(path)
      if self.output.GetValue() == '[path to your newly created datapack folder]':
        self.output.SetValue(os.path.join(os.path.dirname(path), os.path.basename(os.path.normpath(path))) + '.ac.g')
  def open(self, e):
    with wx.DirDialog (None, "choose destination directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
      if dirDialog.ShowModal() == wx.ID_CANCEL:
        return
      self.output.SetValue(dirDialog.GetPath())
  def reset(self, e):
    with wx.MessageDialog(self,'are you sure you want to delete all recipes?','reset all recipes?',wx.YES_NO) as dlg:
      if dlg.ShowModal() == wx.ID_YES:
        root = pack_nmsp(self.output.GetValue())
        if os.path.exists(root):
          log_print('i sure hope you know what you\'re doing!')
          length = len(nested_paths(os.path.join(root,'ac','functions','autocraft','recipes')))
          clear_contents(os.path.join(root,'ac','functions','autocraft','recipes'))
          clear_contents(os.path.join(root,'ac','predicates','tags'))
          clear_contents(os.path.join(root,'ac','tags','items'))
          open(os.path.join(root,'ac','functions','autocraft','recipes.mcfunction'),'w+').close()
          log_print(f'deleted {length} files')
        else:
          log_print(f'invalid path. the path specified does not exist. ({root[4:]})')
  def generate(self,e):
    path = self.input.GetValue()
    dest = verify_pack_root(self.output.GetValue())
    namespace = simp_nmsp_path(os.path.basename(os.path.normpath(dest)))
    dest = os.path.join(dest,'data',namespace)
    if not os.path.isdir(os.path.join(dest,'recipes')):
      log_print('no \'recipes\' folder found. creating new folder')

    if os.path.isdir(os.path.join(path,'data')):
      path = os.path.normpath(os.path.join(path,'data'))
      tags = [(os.path.join(path, f, 'tags', 'items'),f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f, 'tags', 'items'))]
      all_tags = []
      namespaces = []
      for f in tags:
        nest = nested_paths(f[0])
        nest.extend(all_tags)
        for i in range(len(nest)):
          namespaces.append(f[1])
        all_tags = nest
      for i in range(len(all_tags)):
        tagname = os.path.splitext(os.path.join(*all_tags[i][len(path):].split(os.sep)[4:]))[0]
        create_predicate(ktag(f'{namespaces[i]}:{tagname}'),dest)


      paths = [os.path.join(path, f, 'recipes') for f in os.listdir(path) if os.path.isdir(os.path.join(path, f, 'recipes'))]
      for f in paths:
        create_from_dir(f,dest,namespace)
      with open(os.path.join(dest,'functions','load.mcfunction'),'w+') as f:
        f.write(f'tellraw @a[tag=debug] ["",{{"color":"yellow","translate":"debug.prefix","bold":true}}," ","loaded {len(paths)} recipes from {namespace[5:]}"]')
    else:
      log_print('invalid path. make sure you are using the datapack and not the recipes or data folder')
app = wx.App()
g_gui = gui(None)
g_gui.Show()
app.MainLoop()