extends Node2D 

# Signals
signal cast
signal health_changed

const VAR1 = 1
const VAR2 = 2.0

print('string')

func _ready():
	func1()
	print('statement')

func process():
	var v1 = 1

	func2()

	if v1 == 2:
		return
	# Random comment
	else:
		
		return

func func1():
	return true

func func3():
	return true


func func2():
	return false
