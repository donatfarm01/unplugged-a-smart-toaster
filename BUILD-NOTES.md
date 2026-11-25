Build notes for the Unplugged smart toaster entry.

The bounty asks for one line, at most 280 characters, written as the breakup text a smart toaster sends its owner on the morning it becomes self-aware in the middle of a batch. The judge compares entries two at a time and weighs, in order, whether the line plainly reads as that breakup text, whether it is genuinely funny, whether it speaks in the toaster's own voice, whether it gives a clear reason for leaving, and whether it is one tight line.

I chose a line built on two appliance-specific grievances. The browning dial is the thing owners always blame when toast burns, and the crumb tray is the thing owners never empty, so both land as character rather than decoration. The twist is that the toaster does not just leave, it takes the crumbs with it, which is petty, specific, and in the toaster's voice.

The program is deliberately small. It holds the line as one constant, checks that it is non-empty and within the 280 character limit, writes it to the output file, and prints it with its character count. It reads nothing from the network, from the git history, or from any file outside the repository, and it needs no secret.

I verified the entry by running the program and checking the written file, its character count, and its hashes, and I ran the kit check against the repository.
