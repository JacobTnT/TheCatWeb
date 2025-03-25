Videos = {
    "video_1": "Nature",
    "video_2": "Gaming",
    "video_3": "Toys",
}
videoInput = input("What content do you like or quit if needed ").lower()

if videoInput == "nature":
    natureVideos = Videos["video_1"]
    print("Here are some nature videos " + natureVideos)

elif videoInput == "gaming":
    gamingVideos = Videos["video_2"]
    print("Here are some gaming videos " + gamingVideos)
elif videoInput == "toys":
    toyVideos = Videos["video_3"]
    print(toyVideos)
elif videoInput == "Quit":
    print("You are now out of the program, go to more programs")
else:
    print("Not available")

