from create import makeBuild
from song import makeSong


def launchApp():
    pick = input("A. Add a new band, or \nB. Make a new song\n")

    # Will be improved when we move to a web format
    if (pick.lower() == "a"):
        makeBuild()
    elif (pick.lower() == "b"):
        makeSong(None)
    else:
        print("\nPlease select either A or B")
        launchApp()

if __name__ == "__main__":
    print("Welcome to the Song Master 9000\nWould you like to...")
    launchApp()
