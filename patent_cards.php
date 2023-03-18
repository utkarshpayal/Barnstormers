<?php

// Connect to the database
$conn = mysqli_connect('localhost', 'root', 'Manjeet3843a', 'patents');

// Query to fetch the patent information
$sql = "SELECT TITLE_OF_INVENTION, PUBLICATION_DATE, FIELD_OF_INVENTION, APPLICATION_NUMBER FROM patents_info";

// Execute the query
$result = mysqli_query($conn, $sql);

// Loop through the result set and generate the card design for each patent
while ($patent = mysqli_fetch_array($result)) {
    echo '<div class="col-md-4">
            <div class="card mb-4 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">' . $patent[0] . '</h5>
                    <p class="card-text">Publication Date: ' . $patent[1] . '</p>
                    <p class="card-text">Field of Invention: ' . $patent[2] . '</p>
                    <p class="card-text">Publication Number: ' . $patent[3] . '</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                            <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                        </div>
                        <small class="text-muted">9 mins</small>
                    </div>
                </div>
            </div>
        </div>';
}

// Close the database connection
mysqli_close($conn);

?>
