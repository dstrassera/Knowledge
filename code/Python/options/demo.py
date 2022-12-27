import argparse


class MyMainModel:
    __slots__ = ('parser', 'y', 'z', 'opt')

    def __init__(self, y, z):
        self.parser = argparse.ArgumentParser(add_help=False)
        self.parser.add_argument('--model_name', type=str, default="BaseModel")
        self.opt = self.parser.parse_args()
        self.y = y
        self.z = z


class MyChildModelA(MyMainModel):
    __slots__ = ('parser', 'i', 'a', 'opt')

    def __init__(self, MyMainModel, i, a):
        super().__init__(MyMainModel.y, MyMainModel.z)
        self.a = a
        self.i = i
        self.parser = self.get_child_model_options()
        self.opt = self.parser.parse_args()

    def get_child_model_options(self):
        parser = argparse.ArgumentParser(parents=[self.parser])
        parser.add_argument('--child_options_a', type=str, default="Child_A")
        return parser


class MyChildModelB(MyMainModel):
    __slots__ = ('parser', 'i', 'a', 'opt')

    def __init__(self, MyMainModel, i, a):
        super().__init__(MyMainModel.y, MyMainModel.z)
        print(self.parser)
        self.a = a
        self.i = i
        self.parser = self.get_child_model_options()
        self.opt = self.parser.parse_args()

    def get_child_model_options(self):
        parser = argparse.ArgumentParser(parents=[self.parser])
        parser.add_argument('--child_options_b', type=str, default="Child_B")
        return parser


if __name__ == "__main__":
    base = MyMainModel(0,1)
    ca = MyChildModelA(base,2,3)
    cb = MyChildModelB(base,4,5)
    try:
        print("Trying to add something not-declared to my objects....")
        base.w = "Hello"
    except:
        print("An Exception has been raised")
    finally:
        print("----------------------------")
    print("Base    -->", base.opt)
    print("--------------")
    print("Child A -->", ca.opt)
    print("--------------")
    print("Child B -->", cb.opt)
    print("--------------")
    print("End")
