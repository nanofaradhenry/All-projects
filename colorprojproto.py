print("Hello World ")
print("welcome to project")
brn =['1','2','7','8','13','14','19','20','25','26','31','32','37','38','43','44','49','50','55','56','61','62','67','68']
org=['3','4','9','10','15','16','21','22','27','28','33','34','39','40','45','46','51','52','57','58','63','64','69','70']
yel=['5','6','11','12','17','18','23','24','29','30','35','36','41','42','47','48','53','54','59','60','65','66','71','72']


li = 1
for i in range(1, 72, 2):
    if li == 1:
        brn.append(str(i))
        brn.append(str(i + 1))
    elif li == 2:
        org.append(str(i))
        org.append(str(i + 1))
    else:
        yel.append(str(i))
        yel.append(str(i + 1))
    li += 1
    if li > 3:
        li = 1