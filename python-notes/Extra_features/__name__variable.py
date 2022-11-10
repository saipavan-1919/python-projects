"""
    __name__:
        * __name__ is a special varible which tells us if the file is being imorted or running directly.
        * if __name__ value is equal to "__main__" that means the file is being directly
        * otherwise it is being imported in another file and calling this file.
        * Generally python code doesn't consist of any main function to start executing 
        * In python the code starts executing at which code has zero indentation.

        * __name__ will primarily indicate whether the file is being imported or directly executing
         __name is a special variable in python

        ex1: 
            f1.py

                print("f1 __name__ = ",__name__)
                if __name__ == "__main__":
                    print("f1 Running directly")
                else:
                    print("f1 i'm imported")

        ex2:
            f2.py
                import f1

                print("f2 __name__ = ",__name__)
                if __name__ == "__main__":
                    print("f2 Running directly")
                else:
                    print("f2 i'm imported")

        * When we execute f1.py 
        o/p = __main__
              f1 running directly
        
        * when we execute f2.py
        o/p = f1
              f1 i'm imported
              __main__
              f2 runnign directly
                    

"""
