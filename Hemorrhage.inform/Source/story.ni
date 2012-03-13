"Hemorrhage" by Ben Leiken

[Custom Actions]
Wiring it with is an action applying to two things. Understand "wire [something] with [something]" as wiring it with.
Dosing it with is an action applying to two things. Understand "dose [something] with [something]" as dosing it with.

[Custom Attributes]
A thing can be wired or unwired.
A thing can be dosed or undosed.

[Starting Conditions]
The player is in the Left Atrium.

When play begins, say "You are a Macrophage named Phil. You live inside of Ming Chow. Ming has a brain aneurysm. His life is in YOUR flagelli (hands). You must save him before his time runs out!"

[Rooms, Objects, Doors]
The Left Atrium is a lighted room. The description of the Left Atrium is "The Atrium pulsates all around you, pumping red and white blood cells, platelets, and plasma southward towards the Right Ventricle." The Electrostatic Stimulator is here.

The Left Ventricle is a lighted room. The description of the Left Ventricle is "The pulsation is more powerful here, as blood is directed westward through the aortic valve, into the aorta, and into the brain. To the east is the pulmonary vein." The Pulmonary Vein is east of the Left Ventricle.

The Pulmonary Vein is a lighted room. The description of the Pulmonary Vein is "Oxygenated blood rushes past you towards the Left Ventricle. The Lungs are to the east." There is a Half sign in the Pulmonary Vein. The description of the Half-Sign is "To correctly repair the aneurysm, you must use a heparin capsule. To administer the heparin, use the custom command--dose aneurysm with heparin."

The Lungs is a lighted room. The description of the Lungs is "You witness Oxygen Molecules moving out of the Lungs and into the bloodstream." The Lungs is east of the Pulmonary Vein.


The Right Ventricle is a lighted room. The description of the Right Ventricle is "The ventricle is pulsating loudly as deoxygenated blood rushes past you into the pulmonary arteries. The Left Ventricle is to the north. The Inferior Vena Cava is to the south." The Right Ventricle is south of the Left Ventricle. The Right Ventricle is north of the Inferior Vena Cava.

The Inferior Vena Cava is a lighted room. The description of the Inferior Vena Cava is "Blood rushes past you towards the Right Ventricle. The Stomach is to the south." 

The Stomach is a lighted room. The description of the Stomach is "Food particles, acids, and enzymes churn around you. Don't stay here long!" The Stomach is south of the Inferior Vena Cava. There is a Other-Half Sign in the Stomach. The description of the Other-Half Sign is "To repair the aneurysm you must use the wire coil! Repair it by using the custom command -- wire the aneurysm with coil!"


The Aorta is a lighted room. The description of the Aorta is "The pressure in here is incredible! The Cerebral Cortex is ahead." The cholesterol deposit is a container in the Aorta. The cholesterol deposit is fixed in place, closed, and openable.

The Aortic Valve is a door. The Aortic Valve is west of the Left Ventricle and south of the Aorta. The Aortic Valve is unlocked.

 The leaflet is in the cholesterol deposit. The description of the leaflet is "The aneurysm is located ahead! You must find the heparin capsule and the wire coil! Hurry, Ming doesn't have much time!"


The Cerebral Cortex is a lighted room. The description of the Cerebral Cortex is "There is a bulging, pulsating mass on the ceiling. It's the aneurysm!" The Aneurysm is in the Cerebral Cortex. The Aneurysm is unwired, undosed, and fixed in place.
The Mitral Valve is a door. The Mitral Valve is south of the Left Atrium and north of the Left Ventricle. The Mitral Valve is locked. The matching key of the Mitral Valve is the Electrostatic Stimulator.

The Aorta is north of the Aortic Valve.

The calcium deposit is in the Cerebral Cortex. The description of the calcium deposit is "A hard, white block of calcium. Maybe this is valuable to someone?"
 
The Cerebral Cortex is north of the Aorta.

The Cerebellum is a lighted room. The description of the Cerebellum is "You are in the control center of Ming. Be careful, don't touch anything!" The Cerebellum is north of the Cerebral Cortex. 

The G-Protein Coupled Receptor is a door. The G-Protein Coupled Receptor is north of the Cerebellum and south of the Salivary Gland. The G-Protein Coupled Receptor is locked. The matching key of the G-Protein Coupled Receptor is the G-P.

The Salivary Gland is a lighted room. The description of the Salivary Gland is "It's salty and moist in here. Saliva drips off the walls."  The Salivary Gland is north of the G-Protein Coupled Receptor. The heparin capsule is here.

[Objective actions]
Instead of wiring the Aneurysm with wire coil:
	say "The Aneurysm has been wired!";
	move the wire coil to Aneurysm;
	increase the score by 100;
	change Aneurysm to wired.
	
Instead of dosing the Aneurysm with heparin capsule:
	say "The Aneurysm has been dosed with Heparin!";
	move the heparin to Aneurysm;
	increase the score by 100;
	change the Aneurysm to dosed.
[Rules]	
Every turn:
	If Aneurysm is wired and Aneurysm is dosed begin;
	change Aneurysm to dosed;
	say "The Aneurysm has been treated! Ming will live.";
	end the game in victory;
	end if.
	
Every turn:
	If the player is carrying the Lysosome begin;
	decrease the score by 20;
	say "You are still holding the lysosome!!! It's dissolving your membrane -- better drop it.";
	end if.

[Cast of Characters]
James the Amoeba is a man. James the Amoeba is in the Left Ventricle. The description of James the Amoeba is "A lumpy, surly-looking Amoeba. He asks you to find him a calcium deposit."
Instead of giving the calcium deposit to James the Amoeba:
	say "Now James has the calcium deposit. He is delighted!";
	move the calcium deposit to James the Amoeba;
	increase the score by 50.

Alex the Interneuron is a man. Alex the Interneuron is in the Cerebellum. The description of Alex the Interneuron is "A friendly-looking Interneuron. He tells you he has the G-Protein". Alex the Interneuron is carrying the G-P.
Instead of asking Alex the Interneuron for the G-P:
	say "Now you have the G-Protein!";
	move the G-P to the player;
	increase the score by 50.
	
John the Virus is a man. John the Virus is in the Cerebellum. The description of John the Virus is "A shifty-looking Virus. He is holding a lysosome…". John the Virus is carrying the Lysosome.
Instead of asking John the Virus for the Lysosome:
	move the lysosome to the player;
	say "You have been dissolved by the Lysosome!!!!!!! Luckily a friendly macrophage brings you back from the brink.";
	decrease the score by 200.
	
Don the Macrophage is a man. Don the Macrophage is in the Lungs. The description of Don the Macrophage is "Your friend Don greets you warmly. He tells you he has a wire coil that he thinks you'll need." Don the Macrophage is carrying the wire coil.
Instead of asking Don the Macrophage for the wire coil:
	say "You have the wire coil! You're one step closer to repairing the aneurysm";
	move the wire coil to the player;
	increase the score by 50.
Josh the Flesh-Eating Bacteria is a man. Josh the Flesh-Eating Bacteria is in the Stomach. The description of Josh the Flesh-Eating Bacteria is "Josh eyes you angrily and asks if you're lost because there's not much of use in here."



