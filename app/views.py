from app import app
from flask import Flask, render_template, request, abort, Markup
import sqlite3

@app.route('/')
@app.route('/home')
def home():
	return render_template('base.html')

@app.route('/projection', methods = ['POST'])
def projection():
	income = int(request.form['income'])
	fixed = int(request.form['fixed'])
	food = int(request.form['food'])
	shopping = int(request.form['shop'])
	other = int(request.form['other'])
	debt = int(request.form['debt'])
	time = int(request.form['time'])
	total = fixed+food+shopping+other
	spare = income - total
	print total
	print spare
	#current rate user will pay off debt
	current_rate = debt/spare
	#monthly required payment to pay off in desired time
	desired_rate_pay = debt/time
	#check if rate is possible
	match_rate = spare-desired_rate_pay

	if match_rate < 0:
		negative = match_rate
		print str(negative).replace('-', '$'), 'off from desired goal.'
		print 'Make adjustments'
	elif match_rate > 0:
		surplus = match_rate
		print 'On track'
	else:
		print 'On track'
	#calculate percentage and change into new budget
	#shift shopping then food then other
	save_debt = negative * -1

	print save_debt

	flexible = sorted([food, shopping, other])
	high_flexible = flexible[0]


	percentage_debt = save_debt/100

	if percentage_debt*50 > high_flexible:
		print 'Not plausible saving time...'
	else:
		new_high = 

	# shop_adj = percentage_debt*75
	# food_adj = percentage_debt*15
	# other_adj = percentage_debt*10





