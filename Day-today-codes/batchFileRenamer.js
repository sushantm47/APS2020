const path = require("path");
const fs = require("fs");

const directoryPath = path.join(__dirname);
let i = 0;
const filenames = [];
console.log(directoryPath);
fs.readdir(directoryPath, function (err, files) {
  if (err) {
    console.log("Error getting directory information.");
  } else {
    files.forEach(function (file) {
      //   console.log(file);
      i += 1;
      filenames.push(file);
      name = file.split(".");
      nameSlice = name[0].slice(2);
      newName = nameSlice.replace(/_/g, "-") + "__" + i + "." + name[1];
      fs.rename(oldPath, newPath, function (err) {
        if (err) throw err;
        console.log("File Renamed.");
      });
    });
  }

  console.log(filenames);
});
