var fileInput = document.getElementById("csv");
console.log("console log 1 for fileinput =" + fileInput)


    readFile = function () {
        var reader = new FileReader();
        reader.onload = function () {
            document.getElementById('out').innerHTML = reader.result;
        };
        // start reading the file. When it is done, calls the onload event defined above.
        reader.readAsBinaryString(fileInput.files[0]);
    };

fileInput.addEventListener('change', readFile);
console.log("fileInput" + fileInput)
console.log("readFile" + readFile)