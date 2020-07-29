var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
function templateHTML(path){
<<<<<<< HEAD
    data = fs.readFileSync(path,'utf-8');
    return data;
}

var app = http.createServer(function(request,response){
    var _url = request.url;
    var pathname = url.parse(_url,true).pathname;
    if(pathname == '/'){
         response.writeHead(200);
         response.end(templateHTML('./html/sign_in/index.html'));
    }
})

app.listen(3001);
=======
	data = fs.readFileSync(path,'utf-8');
	return data;
}

var app = http.createServer(function(request,response){
   var _url = request.url;
   var pathname = url.parse(_url,true).pathname;

    if(pathname == '/'){
         response.writeHead(200);
		 var template = templateHTML('./html/index.html');
		 console.log(template);
         response.end(template);
    }
})

app.listen(9000);
>>>>>>> 2f6f3b70b92eebbeed4c8b31628c77d5142d958b
