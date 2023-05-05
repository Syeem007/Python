item = ["po01", "po02", "po03", "po04", "po05", "po06", "po07", "po08", "po09", "po11", "po11", "po12"]
for i in item:
  print(fr"connection.send_command(show mac address-table interface {i})")