# with out any init and str methods

class Python:
    def lang (self,version,name):
        self.version = version
        self.name = name
    def display(self):
        return f"{self.version} {self.name}"

class Java:
    def lang (self,version,name):
        self.version = version
        self.name = name
    def display(self):
        return f"{self.version} {self.name}"

python = Python()
python.lang(3.10,"PYTHON")
print(f"{python.display()}")

java = Java()
java.lang(3.15,"JAVA")
print(f"{java.display()}")

# with init and str methods

class Python:
    def __init__(self,version,name):
        self.version = version
        self.name = name
    def __str__(self):
        return f"Version : {self.version} \nName : {self.name}"

class Java:
    def __init__(self,version,name):
        self.version = version
        self.name = name
    def __str__(self):
        return f"Version : {self.version} \nName : {self.name}"

python = Python(3.10,"PYTHON")
print(python)
java = Java(3.15,"JAVA")
print(java)