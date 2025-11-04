import tkinter as tk


class Calculation():
    buttons = [
        ('C', 1, 0), ('←', 1, 1), ('%', 1, 2), ('÷', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
        ('*', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)]
    
    calculationSymbol = ['+', '-', '×', '÷', '%', "."]

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("计算器")
        self.calculationDisplayBox = tk.StringVar()
        self.str1 = "0"
        self.calculationDisplayBox.set(self.str1)
        self.root.resizable(0, 0)
        self.root.attributes("-topmost", True)
        self.calculationDisplay = tk.Entry(self.root, textvariable=self.calculationDisplayBox, 
                                          font=("Arial", 20), state="readonly")
        self.calculationDisplay.grid(columnspan=4, sticky="NSEW")
        self.buttonInterface()
        self.root.mainloop()

    def buttonInterface(self):
        for i in self.buttons:
            if i[0] == "C":
                self.button(text=i[0], column=i[2], row=i[1], command=self.clear, root=self.root)
            elif i[0] == "←":
                self.button(text=i[0], column=i[2], row=i[1], command=self.delete, root=self.root)
            elif i[0] == "=":
                self.button(text=i[0], column=i[2], row=i[1], command=self.calculation, root=self.root)
            elif i[0] == ".":
                self.button(text=i[0], column=i[2], row=i[1], 
                           command=lambda t=i[0]: self.add_xsd(t), root=self.root)
            elif i[0] in self.calculationSymbol:
                self.button(text=i[0], column=i[2], row=i[1], 
                           command=lambda t=i[0]: self.symbolJudgment(t), root=self.root)
            else:
                self.button(text=i[0], column=i[2], row=i[1], 
                           command=lambda t=i[0]: self.add_str(t), root=self.root)

    def button(self, text: str, column: int, row: int, command, root):
        button = tk.Button(root, text=text, command=command, width=5, height=2)
        button.grid(column=column, row=row, padx=2, pady=1)

    def clear(self):
        self.calculationDisplayBox.set("0")
        self.str1 = "0"

    def delete(self):
        self.str1 = self.str1[:-1]
        if self.str1 == "":
            self.str1 = "0"
        self.calculationDisplayBox.set(self.str1)
        self.root.update()

    def add_str(self, str1):
        if self.str1 == "0" and str1 == "0":
            pass
        else:
            if self.str1 == "0" and str1 != ".":
                self.str1 = ""
            try:
                if self.str1[-2] in self.calculationSymbol[:-1] and self.str1[-1] == "0" and str1 != ".":
                    pass
                else:
                    self.str1 += str1
                    self.calculationDisplayBox.set(self.str1)
                    self.root.update()
            except IndexError:
                self.str1 += str1
                self.calculationDisplayBox.set(self.str1)
                self.root.update()

    def calculation(self):
        if self.str1:
            for i in range(len(self.str1)):
                if i + 1 == len(self.str1):
                    break
                if self.str1[i] == "%" and self.str1[i + 1] in self.calculationSymbol:
                    self.str1 = self.str1[:i + 1] + "1" + self.str1[i + 1:]

            if self.str1[-1] == "%":
                self.str1 = self.str1[:-1]
                self.str1 += "/100×1"
            elif self.str1[-1] in self.calculationSymbol:
                self.str1 = self.str1[:-1]

            try:
                self.str1 = self.str1.replace("*", "**")
                self.str1 = self.str1.replace("÷", "/")
                self.str1 = self.str1.replace("×", "*")
                self.str1 = self.str1.replace("%", "/100*")

                self.str1 = str(eval(self.str1))

                if "." in self.str1 and self.str1[-1] == "0":
                    self.str1 = self.str1[:-2]

                self.calculationDisplayBox.set(self.str1)
                self.str1 = "0"

            except ZeroDivisionError:
                self.calculationDisplayBox.set("除数不能为0")
                self.str1 = "0"
            except ValueError:
                self.calculationDisplayBox.set("数学运算超出定义域")
                self.str1 = "0"
            except OverflowError:
                self.calculationDisplayBox.set("计算的数字过大")
                self.str1 = "0"
            except SyntaxError:
                self.calculationDisplayBox.set("表达式不合法")
                self.str1 = "0"

    def symbolJudgment(self, str1):
        if self.str1:
            if self.str1[-1] == "%":
                self.str1 += str1
            elif self.str1[-1] in self.calculationSymbol:
                pass
            else:
                self.str1 += str1
            self.calculationDisplayBox.set(self.str1)
        else:
            self.calculationDisplayBox.set("0")

    def add_xsd(self, str1):
        if self.str1 == "0":
            self.str1 += str1
            self.calculationDisplayBox.set(self.str1)

        if self.str1 != "0":
            can_add_dot = True
            for i in self.str1[::-1]:
                if i in self.calculationSymbol:
                    if i == ".":
                        can_add_dot = False
                        break
                    else:
                        break

            if can_add_dot:
                self.str1 += str1
                self.calculationDisplayBox.set(self.str1)


if __name__ == "__main__":
    root = Calculation()
