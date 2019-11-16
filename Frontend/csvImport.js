var fileInput = document.getElementById("csv"),


    readFile = function () {
        var reader = new FileReader();
        reader.onload = function () {
            //document.getElementById('out').innerHTML = reader.result;
            table = reader.result 
            csvAsArray = reader.result.csvToArray();
            console.log(csvAsArray)
        };
        // start reading the file. When it is done, calls the onload event defined above.
        reader.readAsBinaryString(fileInput.files[0]);
        
    };

fileInput.addEventListener('change', readFile);
// Empty array called table that will be populated with the imported csv data.
var table = [];  

var csvAsArray 