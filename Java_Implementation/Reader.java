import java.io.*;
import java.util.*;

public class Reader {
    
    static int[] special = {1,12,23,34,45,56,68,79,90,101,112};
    static double ratio1 = 0.149253731;
    static double ratio2 = 0.022276676;
    
    public static void main(String[] args) throws IOException{ //throw exception due to file reading
        File file = new File(".");
        File[] files = file.listFiles();  
        List<String> relevantfiles = new ArrayList<String>();
        for (File file1 : files) {
            String[] parts = file1.toString().split("\\.");
            if (parts[parts.length-1].equals("txt")){
                String[] parts2 = parts[1].split("");
                String name = "";
                for(int i = 1;i < parts2.length;i++){
                    name = name + parts2[i];
                }
                relevantfiles.add(name);
            } 
            } 
        // scan all avaiable files
        for (int i = 0; i < relevantfiles.size(); i++ ){
            relevantfiles.set(i, relevantfiles.get(i) + ".txt"); 
        }
	\\ choose file that is read from the ones available in the directory
        while(true){
            System.out.print("These are the available files. ");
            System.out.println("Please choose the one you are interested in!");
            for(int i = 0; i < relevantfiles.size();i++){
                System.out.println(i + " ... " + relevantfiles.get(i));
            }
            Scanner scanner = new Scanner(System.in);
            String input1 = scanner.next();        
            try{
                int value = Integer.parseInt(input1);
                relevantfiles.set(0,relevantfiles.get(value)); // chosen value
                break;
            }
            catch(IllegalArgumentException e){
                System.out.println(input1 + " is not an integer!");
            }
            catch(IndexOutOfBoundsException e2){
                System.out.println(input1 + " is not an allowed value!");
            }
        }
        List<Double> helpresult = new ArrayList<Double>(); //  save each time step
        double counter = 0;
        int countercells = 0; //check number of scanned cells for each timestep
        int oil = 0; // helper variable
        int[] helper = {0};
        // read each line and process it accordingly 
        BufferedReader input = new BufferedReader(new FileReader(relevantfiles.get(0)));
        String line;
        while((line = input.readLine()) != null){ // read line by line
            line = line.trim();
            String[] text = line.split(" ");
            text = nospace(text);
            if (text.length > 1){ //ignore empty lines
                if ((text[1]).equals("Days")){ // a new time step is starting, save all counters and set them to zero
                helpresult.add(counter);
                System.out.println(countercells);
                counter = 0;
                countercells = 0;
                }
                // start oil segment
                if(text[0].equals("Oil") && text[1].equals("Saturation")){ 
                    oil = 1;
                }
                // end oil segment
                if(text[0].equals("Gas") && text[1].equals("Saturation")){
                    oil = 0;
                }
                // oil active
                if(oil==1){
                    if(text[0].equals("Plane")){
                        if (text.length > 4 && text[5].equals("All")){
                            counter = counter + 111*111*Double.parseDouble(text[7]);
                            countercells = countercells + 111*111;
                            System.out.println("Yes");
                        }
                    }
                    // header
                    if(text[0].equals("I")){
                        if(text[2].equals("99") == false)
                            helper = getlist(text[2]);
                        else
                            helper = getlist("99");                   
                    }
                    if(text[0].equals("J=")){           // standard line
                        counter = counter + getcounter1(text,helper);
                        countercells = countercells + text.length-2;
                    }
                    if(text.length > 2 && text[0].length() > 2 && text[0].charAt(0)== 'J' && text[0].charAt(2) == '1'){
                        counter = counter + getcounter2(text,helper);
                        countercells = countercells + text.length-1;
                    }
                
                    
                } // end of oil active
            } // end of ignore empty lines
        } // end of line reader
        // write recorded data into an output file
        FileOutputStream writer = new FileOutputStream("output.txt");
        double original = helpresult.get(0);
        for(double d : helpresult){ // write each line to output file, necessary to convert in to bytes for that
            byte[] contentinbytes = (Double.toString((1.0 - d/original)*100) + System.lineSeparator()).getBytes();
            writer.write(contentinbytes);
        }
    } // end of main method
    
    public static int[] getlist(String t){
        int first = Integer.parseInt(t);
        int[] output = new int[14];
        for(int i = first;i < first+14;i++){
            output[i-first] = i;
        }
        return output;
    } 
    
    public static double getcounter1(String[] text, int[] helper){
        int value = Integer.parseInt(text[1]);
        double result = 0;
        if(in(special,value)){
            for(int i = 2; i < text.length; i++){
                if(in(special,helper[i-2]))
                    result = result + ratio1*Double.parseDouble(text[i]);
                else
                    result = result + ratio2*Double.parseDouble(text[i]);
            }
        }
        else
            for(int i = 2; i < text.length; i++){
                if(in(special,helper[i-2]))
                    result = result + ratio1*Double.parseDouble(text[i]);
                else
                    result = result + Double.parseDouble(text[i]);
            }
        return result;
    }
    
    public static double getcounter2(String[] text, int[] helper){
        char a = text[0].charAt(2);
        char b = text[0].charAt(3);
        char c = text[0].charAt(4);
        String h1 = new StringBuilder().append(a).append(b).append(c).toString();
        int value = Integer.parseInt(h1);
        double result = 0;
        if(in(special,value)){
            for(int i = 2; i < text.length; i++){
                if(in(special,helper[i-2]))
                    result = result + ratio1*Double.parseDouble(text[i]);
                else
                    result = result + ratio2*Double.parseDouble(text[i]);
            }
        }
        else
            for(int i = 2; i < text.length; i++){
                if(in(special,helper[i-2]))
                    result = result + ratio1*Double.parseDouble(text[i]);
                else
                    result = result + Double.parseDouble(text[i]);
            }
        return result;
    }
    
    public static boolean in(int[] array, int value){
        for(int i = 0; i < array.length; i++){
            if(array[i] == value)
                return true;
        }
        return false;
    } 
    
    public static String[] nospace(String[] input){
        int counter = 0; 
        for(String i : input){
            if(i.equals("") == false)
                counter++;
        }
        String[] output;
        output = new String[counter];
        counter = 0;
        for(String i : input){
            if(i.equals("") == false){
                output[counter] = i;
                counter++;
            }
        }
        return output;
    }
    
} // end of class
