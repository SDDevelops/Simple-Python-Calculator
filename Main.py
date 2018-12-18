from tkinter import *
import solve as solved

#how to use a class to with Tkinter
def main():

    class Application(Frame):

        """ Gui application with 3 methods"""
        def __init__(self,master):
            #inilitilazes the frame

            Frame.__init__(self,master)
            self.grid()
            self.equation = ""

            self.keyPad()

        #Shows the keypad
        def keyPad(self):

            Label(self, text="Calculator Program",width = "19", height = "1", bg = "red" , justify = CENTER ).grid(row=0, columnspan=4, sticky=W+E)

            self.EQ_entry = Text(self,width = 10,height = 1, wrap =WORD)
            self.EQ_entry.grid(row=1, columnspan=4, sticky=W+E)

            Button(self, text=" 1 ",command = lambda: self.add_Item(1), width = "4", height = "2").grid(row = 3, column = 0, sticky = 'W')
            Button(self, text=" 2 ",command = lambda: self.add_Item(2), width = "4", height = "2").grid(row = 3, column = 1, sticky = W )
            Button(self, text=" 3 ",command = lambda: self.add_Item(3), width = "4", height = "2").grid(row = 3, column = 2, sticky = 'W')
            Button(self, text=" * ",command = lambda: self.add_Item("*"), width = "4", height = "2").grid(row = 3, column = 3, sticky = 'W')

            Button(self, text=" 4 ",command = lambda: self.add_Item(4), width = "4", height = "2").grid(row = 4, column = 0, sticky = 'W')
            Button(self, text=" 5 ",command = lambda: self.add_Item(5), width = "4", height = "2").grid(row = 4, column = 1, sticky = 'W')
            Button(self, text=" 6 ",command = lambda: self.add_Item(6), width = "4", height = "2").grid(row = 4, column = 2,sticky = 'W')
            Button(self, text=" / ",command = lambda: self.add_Item("/"), width = "4", height = "2").grid(row=4, column=3, sticky='W')

            Button(self, text=" 7 ",command = lambda: self.add_Item(7), width = "4", height = "2").grid(row = 5, column = 0, sticky = 'W')
            Button(self, text=" 8 ",command = lambda: self.add_Item(8), width = "4", height = "2").grid(row = 5, column = 1, sticky = 'W')
            Button(self, text=" 9 ",command = lambda: self.add_Item(9), width = "4", height = "2").grid(row = 5, column = 2, sticky = 'W')
            Button(self, text=" + ",command = lambda: self.add_Item("+"), width = "4", height = "2").grid(row=5, column = 3, sticky = 'W')


            Button(self, text=" 0 ",command = lambda: self.add_Item(0), width = "4", height = "2").grid(row=6, column = 1, sticky = 'W')
            Button(self, text=" = ",command = lambda: self.solve(), width = "4", height = "2").grid(row=6,column = 2, sticky='W')
            Button(self, text=" - ", command=lambda: self.add_Item("-"), width = "4", height = "2").grid(row=6,column = 3, sticky='W')

            Button(self,text ="C", width = "4", height = "2", command= lambda:self.clear()).grid(row=6, column = 0, sticky = 'W')


        def add_Item(self,nextNum):


            self.equation = self.equation +str( nextNum)

            self.EQ_entry.delete(0.0,END)
            self.EQ_entry.insert(0.0,self.equation)

        def solve(self):
            equation = solved.solve(self.equation)
            self.EQ_entry.delete(0.0, END)
            self.EQ_entry.insert(0.0, equation )
            self.equation=equation


        def clear(self):
            self.EQ_entry.delete(0.0, END)
            self.EQ_entry.insert(0.0,"")
            self.equation = self.equation*0





    root = Tk()
    root.title("Python buttons")
    root.geometry("150x200")

    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
        main()
