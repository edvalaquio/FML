'use strict';

const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({
	extended: true
}));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '/public')));

app.use(function(req, res, next) {
	console.log(`${req.method} request for '${req.url}'`);
	next();
});

app.use(function(req, res, next) {
	console.log(`${req.method} request for '${req.url}'`);
	next();
});

// app.post('/sendFormData', function(req, res){
// 	// console.log("hello");
// 	console.log(req.body);
// 	res.send("This is from back-end");
// });

var multer = require('multer');
var upload = multer({ dest: '/logs'});

app.post('/sendFormData', upload.single('filename'), getRandomNumbers);

const port = 3000;

var	server = require('http').createServer(app);
server.listen(port, function(){
	console.log("Listening on port: " + port);
});
 var fs = require('fs');

function getRandomNumbers(req, res){

	var file = __dirname + '/' + req.file.filename;

	fs.rename(req.file.path, file, function(err) {
		if (err) {
			console.log(err);
			res.send(500);
		} else {
			// res.json({
			// 	message: 'File uploaded successfully',
			// 	filename: req.file.filename
			// });

		}
	});

	console.log(req.body);
	var spawn = require("child_process").spawn;
	var process = spawn("python", ["./public/assets/test.py"]);
	process.stdout.on('data', function(data){
		// console.log(data.toString());
		var fs = require("fs");
		res.send(data.toString());
	});
	// console.log("this is from getRandomNumbers req: "+req);
	// res.send("{BACKEND}");
}