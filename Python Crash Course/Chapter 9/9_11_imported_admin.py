# 9-11. Imported Admin: Start with your work from Exercise
# 9-8 (page 173). Store the classes User, Privileges, and
# Admin in one module. Create a separate file, make an
# Admin instance, and call show_privileges() to show that
# everything is working correctly.

from Modules.user_admin_privileges import *

admin = Admin("Keith", "Moua", 26, "Male", "Cincinnati")
admin.privileges.privileges = ["add posts", "delete posts", "ban users", "warn users"]
admin.privileges.show_privileges()