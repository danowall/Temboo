from temboo.Library.Google.Gmail import SendEmail
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
sendEmailChoreo = SendEmail(session)

# Get an InputSet object for the Choreo
sendEmailInputs = sendEmailChoreo.new_input_set()

# Set credential to use for execution
sendEmailInputs.set_credential('TembooGmailTest')

# Execute the Choreo
sendEmailResults = sendEmailChoreo.execute_with_results(sendEmailInputs)

# Print the Choreo outputs
print("Success: " + sendEmailResults.get_Success())