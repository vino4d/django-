from django.test import SimpleTestCase as stc
from django.urls import reverse as r

# Create your tests here.
#no. of testcase = total no of unique test function in every single class
#i.e. repeated testfunc also counted if is in dif class.
class hptest(stc):
    #func name must be starts with test
    def test_url_exist_cl(self):
        #client.get() is return client's url response/ also has status_code
        response= self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_url_exist_cl(self):
        response= self.client.get("/home/")
        self.assertEqual(response.status_code,200)
    #to test names of path using reverse
    def test_urlname_exist(self):
        response= self.client.get(r("hp"))
        self.assertEqual(response.status_code,200)
    def test_urlname_exist(self):
        response= self.client.get(r("home"))
        self.assertEqual(response.status_code,200)
    #to check templates, we can use assertTemplateUsed
    def test_templates_name_correct(self):
        response= self.client.get(r("hp"))
        self.assertTemplateUsed(response,"home1.html")
    #to check template content or response contenr, we can use assertContains
    def test_template_content(sel):
        response=sel.client.get(r("hp"))
        sel.assertContains(response,"<h1>HOME</h1>")

class aptest(stc):
    def test_url_exist_cl(self):
        response= self.client.get("/about/")
        self.assertEqual(response.status_code,200)
    def test_urlname_exist(self):
        response= self.client.get(r("ap"))
        self.assertEqual(response.status_code,200)
    def test_templates_name_correct(self):
        response= self.client.get(r("ap"))
        self.assertTemplateUsed(response,"about1.html")
    def test_template_content(sel):
        response=sel.client.get(r("v"))
        sel.assertContains(response,"vvvvvvvv")
    def test_template_content(sel):
        #reverse doesnt work on name of this empty url extension("")
        response=sel.client.get("")
        sel.assertContains(response,"iii")    
