
PROBLEMS = "1 2 3 4 5 6 7 8".split()
SEARCH = "BestFirst BFS DFS".split()
SELECT = "Nada E0 E1 E2 E3 E4 E5 E6".split()
HEURISTIC = "AddReuseHeuristic ZeroHeuristic NumOCsHeuristic".split()

from collections import defaultdict

if __name__ == "__main__":


	runtime = defaultdict(float)
	opened = defaultdict(int)
	expanded = defaultdict(int)
	cost = defaultdict(int)
	decomps = defaultdict(int)
	ratio = defaultdict(float)
	solved = defaultdict(int)

	runtimeList = defaultdict(list)
	openedList = defaultdict(list)
	expandedList = defaultdict(list)
	costList = defaultdict(list)
	decompsList = defaultdict(list)
	ratioList = defaultdict(list)
	solvedList = defaultdict(list)

	lineDict = {0: None, 1: None, 2 : None, 3: runtime, 4: opened, 5: expanded, 6: cost, 7: decomps, 8: None, 9: None, 10: None, 11: solved, 12: ratio}
	itemDict = {3:runtimeList, 4: openedList, 5: expandedList, 6: costList, 7: decompsList, 11: solvedList, 12: ratioList}

	stringName = '{}-{}-{}-{}.txt'

	for selection in SELECT:
		for heuristic in HEURISTIC:
			for search in SEARCH:
				for prob in PROBLEMS:
					try:
						with open(stringName.format(prob, search, selection, heuristic), "r") as filename:
							print(filename)
							if int(prob) == 8:
								print(stringName.format(prob, search, selection, heuristic))

							solvedHere = False
							for i, line in enumerate(filename):
								if lineDict[i] is None:
									continue

								if i == 3:
									if float(line.split()[1]) < 6000:
										solvedHere = True
									if solvedHere:
										lineDict[i][search + heuristic + selection] += float(line.split()[1])
										itemDict[i][search + heuristic + selection].append(float(line.split()[1]))

								else:
									if solvedHere:
										lineDict[i][search + heuristic + selection] += int(line.split()[1])
										itemDict[i][search + heuristic + selection].append(int(line.split()[1]))


								if int(prob) == 8:
									# print this line / number solved.
									if (lineDict[11][search + heuristic + selection]) != 0:
										print(line.split()[0] + '\t' + str(lineDict[i][search + heuristic + selection] \
									                                   /lineDict[11][search + heuristic + selection]))
									else:
										print(line.split()[0] + '\t0')

							# solved

							lineDict[11][search + heuristic + selection] += int(solvedHere)

							# ratio
							if solvedHere:
								lineDict[12][search + heuristic + selection] += lineDict[7][search + heuristic + selection] \
							                                                       / lineDict[6][search + heuristic + selection]

							if int(prob) == 8:
								print("ratio" + "\t" + str(lineDict[12][search + heuristic + selection]))
								print('solved' + '\t' + str(
									lineDict[11][search + heuristic + selection]))


					except:
						continue


	# for prob in PROBLEMS:
	# 	for search in SEARCH:
	# 		for heuristic in HEURISTIC:
	# 			for selection in SELECT:
	# 				try:
	# 					with open(stringName.format(prob, search, selection, heuristic), "r") as filename:
	# 						if int(prob) == 8:
	# 							print(stringName.format(prob, search, selection, heuristic))
	#
	# 						solvedHere = False
	# 						for i, line in enumerate(filename):
	# 							if lineDict[i] is None:
	# 								continue
	#
	# 							if i == 3:
	# 								if float(line.split()[1]) < 6000:
	# 									solvedHere = True
	# 								if solvedHere:
	# 									lineDict[i][search + heuristic + selection] += float(line.split()[1])
	# 									itemDict[i][search + heuristic + selection].append(float(line.split()[1]))
	#
	# 							else:
	# 								if solvedHere:
	# 									lineDict[i][search + heuristic + selection] += int(line.split()[1])
	# 									itemDict[i][search + heuristic + selection].append(int(line.split()[1]))
	#
	#
	# 							if int(prob) == 8:
	# 								# print this line / number solved.
	# 								if (lineDict[11][search + heuristic + selection]) != 0:
	# 									print(line.split()[0] + '\t' + str(lineDict[i][search + heuristic + selection] \
	# 								                                   /lineDict[11][search + heuristic + selection]))
	# 								else:
	# 									print(line.split()[0] + '\t0')
	#
	# 						# solved
	#
	# 						lineDict[11][search + heuristic + selection] += int(solvedHere)
	#
	# 						# ratio
	# 						if solvedHere:
	# 							lineDict[12][search + heuristic + selection] += lineDict[7][search + heuristic + selection] \
	# 						                                                       / lineDict[6][search + heuristic + selection]
	#
	# 						if int(prob) == 8:
	# 							print("ratio" + "\t" + str(lineDict[12][search + heuristic + selection]))
	# 							print('solved' + '\t' + str(
	# 								lineDict[11][search + heuristic + selection]))
	#
	#
	# 				except:
	# 					continue


	print('here')


