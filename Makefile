prepare-mark-start:
	@echo "This is a manual goal. Paste what's on the copy-paste buffer"
	@echo 'f cc "Time-Marker: start" --allow-empty' | pbcopy

prepare-mark-end:
	@echo "This is a manual goal. Paste what's on the copy-paste buffer"
	@echo 'f cc "Time-Marker: end" --allow-empty'
