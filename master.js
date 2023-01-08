

$w.onReady(function () {

});


export function button9_click(event) {
  if($w("#uploadButton3").value.length > 0) {
    $w("#text67").text = "Uploading " + $w("#uploadButton3").value[0].name;
    $w("#uploadButton3").startUpload()
      .then( (uploadedFile) => {
        $w("#text67").text = "Upload successful";
        $w("#image4").src = uploadedFile.url;
      })
      .catch( (uploadError) => {
        $w("#text67").text = "File upload error";
        console.log("File upload error: " + uploadError.errorCode);
        console.log(uploadError.errorDescription);
      });
  } 
  else {
    $w("#text67").text = "Please choose a file to upload.";
  }

}
