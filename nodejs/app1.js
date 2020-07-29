var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');


// view engine setup
var app = http.createServer(function(request,response){
	var _url = request.url;
	var queryData = url.parse(_url,true).query;
	var pathname = url.parse(_url,true).pathname;
	fs.readFile('nav.html','utf-8',function(err,data){
		response.writeHead(200);
		response.end(data);
		console.log(data);
	});
});

app.listen(9000,() => {
		  console.log('9090 listen');
		  })
