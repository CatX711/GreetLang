import gpultim.gph

func st() rt:int[0]{
  
	
def var tries = 0;
  
op("Booting...");

while tries < 6 {
  def var user = readline.op("Hello, welcome to PIE OS. What is your username? ");

  // if username is correct
  if user == "pr0gramme5" {
    def var pass = readline.op("Please enter your password to continue. ");

      
    // if password is correct
    if pass = "sharksurfer23"{ 
       op("Welcome, {!user}");
       end; // ends while loop
    }
       // if password is incorrect
    else {
      op("Incorrect, try again.");
      tries += 1;
     }
   }
    
    // if username is wrong 
   else {
     op("Incorrect, try again.");
     tries += 1;
   }
}
