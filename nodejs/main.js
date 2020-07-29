var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
function templateHTML(path){
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
