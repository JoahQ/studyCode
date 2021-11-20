

def bottle_of_beer(bob):
    """
    Prints 99 Bottle of Beer on the Wall lyrics.
    :param bob: Must be a positive integer.
    :return:
    """

    if bob < 1:
        print("""No more
                 bottles
                 of beer
                 on the wall.
                 No more
                 bottles of
                 beer.
                 """)
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of
             beer on the
             wall. {} bottles
             of beer. Take one
             down, pass it
             around, {} bottles
             of beer on the
             wall.""".format(tmp,
                             tmp,
                             bob))
    bottle_of_beer(bob)


bottle_of_beer(2)
