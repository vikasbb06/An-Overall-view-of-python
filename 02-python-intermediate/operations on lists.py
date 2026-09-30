def main():
    list=["Vikas","Vinod","shivu","gowdru","BS","Surya","Yogesh","UV","BA","mc"]
    list_upper=[name.upper() for name in list]
    print("List is",list_upper)
    ending_a=[name for name in list_upper if name.endswith('A')]
    print("List is",ending_a)
    lower_list=[name.lower() for name in list]
    print("List is ",lower_list)
    replacing=[name.replace('U','V') for name in list_upper]
    print("Replaced List Is",replacing)
    starting=[name for name in list_upper if name.startswith('V')]
    print("Starting With 'V' is",starting)
    tri=[name.encode() for name in list]
    print("Encode list is",tri)
    uni=[i.decode for i in tri]
    print("List is :",uni[0])

if __name__=="__main__":
    main()

