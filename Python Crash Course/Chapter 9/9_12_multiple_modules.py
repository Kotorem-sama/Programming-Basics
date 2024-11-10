# 9-12. Multiple Modules: Store the User class in one
# module, and store the Privileges and Admin classes in a
# separate module. In a separate file, create an Admin
# instance and call show_privileges() to show that everything
# is still working correctly.

from Modules.admin_privileges import *

admin = Admin("Keith", "Moua", 26, "Male", "Cincinnati")
admin.privileges.privileges = ["add posts", "delete posts", "ban users", "warn users"]
admin.privileges.show_privileges()