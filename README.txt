Package de ros2 on utilizes turtlesim per dibuixar un paissatge

En la carpeta ros2_ws utilitzo la commanda 
	colcon build --parallel-workers 4
	ros2 run controller my_node

S'ha de tenir turtlesim obert previament

Falta moure turtle3 amb Pose per dibuixar unes montañes

Com fer un commit al GitHub
	en la carpeta controller
		git add *
		git commit -m "<Comentari dels cambis fets>"
		git push -u origin main
