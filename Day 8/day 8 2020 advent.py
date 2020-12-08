import copy as cp
class gameCon():
    def __init__(self, instructions):
        self.accumulator = 0
        self.instruct = instructions
        self.curInstruct = 0
        self.executed = []
       
    def acc(self, val):
        self.accumulator += val
        self.curInstruct += 1
        
    def jmp(self, val):
        self.curInstruct += val
        
    def nop(self, val):
        self.curInstruct += 1
        
    def execute(self):
        self.switch = {"acc":self.acc, "jmp": self.jmp, "nop": self.nop}
        while True:
            if self.curInstruct in self.executed:
                self.executed = []
                return self.accumulator
            else:
                cur = self.curInstruct
                if cur >= len(self.instruct):
                    self.executed.append(cur)
                else:
                    self.switch[self.instruct[cur][0]](self.instruct[cur][1])
                    self.executed.append(cur)

    def fix(self):
        checked = []
        copy = cp.deepcopy(self.instruct)
        while True:
            for i,inst in enumerate(copy):
                if i in checked:
                    continue
                elif inst[0] == "jmp":
                    self.instruct[i][0] = "nop"
                    val = self.execute()
                    self.accumulator = 0
                    if self.curInstruct == len(self.instruct):
                        return val
                    else:
                        self.curInstruct = 0
                        checked.append(i)
                        self.instruct = cp.deepcopy(copy)
                        break
                elif inst[0] == "nop":
                    self.instruct[i][0] = "jmp"
                    val = self.execute()
                    self.accumulator = 0
                    if self.curInstruct == len(self.instruct):
                        return val
                    else:
                        self.curInstruct = 0
                        checked.append(i)
                        self.instruct = cp.deepcopy(copy)
                        break
            
            
                
file = open("data.txt", "r")
instructions = []
for line in file:
    instruc , val = line.strip().split(" ")
    val = val.replace("+", "")
    instructions.append([instruc, int(val)])
   
game = gameCon(instructions)
print (game.fix())





