class varnith:
  def speak(self):
    print("i am an varnith")

class dog(varnith):
  def speak(self):
    print("i bark")

obj=varnith()
book=dog()
obj.speak()
book.speak()
