func helloworld() rt:userdef[void]{
  op("Hello, world!");                             
}

// Main/Start function

func st() rt:int[0]{
  helloworld();
}

// Output:
// Hello, world!



/* VARATION 2:
 
func helloworld() rt:userdef[]{
  return "Hello, world!";                             
}

func st() rt:int[0]{
  op(helloworld());
}

*/
