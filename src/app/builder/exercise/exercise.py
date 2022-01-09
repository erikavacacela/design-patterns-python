class CodeBuilder:

  def __init__(self, root_name):
    self.fields = []
    self.root_name = root_name

  def add_field(self, type, name):
    self.fields.append({'type': type, 'name': name})
    return self

  def __str__(self):
    join_string = 'class %s:\n' % (self.root_name)
    if not self.fields:
      join_string += '  pass'
    else:
      join_string += "  def __init__(self):\n"
      for field in self.fields:
          join_string += '    self.%s = %s\n' % (field["type"], field["name"])
    return join_string


if __name__ == '__main__':
  cb = CodeBuilder('Person') \
      .add_field('name', '""') \
      .add_field('age', '0')
  print(cb)
