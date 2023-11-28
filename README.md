<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="form-container">
        <form>
            <!-- Section for PAN Number and Company Information -->
            <div class="section">
               <label for="panNumber">PAN Number:</label>
                <input type="text" id="panNumber" name="panNumber">

                <label for="companyName">Company Name:</label>
                <input type="text" id="companyName" name="companyName">

                <label for="contactName">Contact Name (Relationship Manager):</label>
                <input type="text" id="contactName" name="contactName">

                <label for="webAddress">Web Address:</label>
                <input type="url" id="webAddress" name="webAddress">
            </div>

            <!-- Section for Registration Date and Address -->
            <div class="section">
                <label for="regDate">Registration Date:</label>
                <input type="date" id="regDate" name="regDate">

                <label for="companyAddress">Company Address:</label>
                <input type="text" id="companyAddress" name="companyAddress">

                <label for="poBox">P.O. Box:</label>
                <input type="number" id="poBox" name="poBox">

                <label for="emailAddress">E-mail Address:</label>
                <input type="email" id="emailAddress" name="emailAddress">
            </div>

            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>

