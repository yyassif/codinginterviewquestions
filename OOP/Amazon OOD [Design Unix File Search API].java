//from https://leetcode.com/discuss/interview-question/609070/amazon-ood-design-unix-file-search-api
// "static void main" must be defined in a public class.
//filter design pattern tutorial http://www.singhajit.com/filter-design-pattern/


//***AND filter and OR filter for UNIX file system search implemented***
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import static java.util.stream.Collectors.toList;

public class Main {
    public static void main(String[] args) {
        new Main().test();
    }
    private void test(){
        Directory dir = new Directory("root");
        File file1 = new File("abc.txt", "abc.txt content".getBytes());
        File file2 = new File("ddd.txt", "dd".getBytes());
        dir.addEntry(file1);
        dir.addEntry(file2);
        Directory sub_dir = new Directory("sub_dir");
        File file3 = new File("333.txt", "333.txt content".getBytes());
        File file4 = new File("444.xml", "444".getBytes());
        sub_dir.addEntry(file3);
        sub_dir.addEntry(file4);
        dir.addEntry(sub_dir);
        
        SearchParams params = new SearchParams();
        params.extension="xml";
        params.maxSize=20;
        params.minSize=1;
        params.name="444.xml";
        
        SearchDirectory searchDir = new SearchDirectory();
        List<File> resultFiles = new ArrayList();
        resultFiles = searchDir.search(dir, params);
        
        for (File file : resultFiles){
            System.out.println("result:"+file);
        }
    }
    public class SearchDirectory{
        private AndFilter andFilter = new AndFilter(
            new NameFilter(),
            new MinSizeFilter(),
            new MaxSizeFilter(),
            new ExtensionFilter());
        private ORFilter orFilter = new ORFilter(
            new NameFilter(),
            new MinSizeFilter(),
            new MaxSizeFilter(),
            new ExtensionFilter());
        public List<File> search(Directory dir, SearchParams params){
            Queue<Directory> q = new LinkedList();
            q.add(dir);
            Directory folder = new Directory("Temp");
            List<Entry> files = new ArrayList();
            List<File> resultFiles = new ArrayList();
            
            while(!q.isEmpty()){
                folder = q.poll();
                files = folder.getEntries();
                for (Entry entry : files){
                    if (entry.isDirectory()){
                        q.add((Directory)entry);
                    }else{
                        resultFiles.add((File)entry);
                    }
                    System.out.println(entry);
                }
            }
            resultFiles = andFilter.filter(params, resultFiles);
            return resultFiles;
        }
    }
    public interface EntryInterface{
        String getName();
        void setName(String name);
        int getSize();
        boolean isDirectory();
    }
    private abstract class Entry implements EntryInterface{
        protected String name;
        public Entry(String name){
            this.name = name;
        }
        @Override
        public String getName(){
            return name;
        }
        
        @Override
        public void setName(String name){
            this.name=name;
        }
        public String toString(){
            return this.name;
        }
    }
    public class File extends Entry{
        private byte[] content;

        public File(String name,byte[] content) {
            super(name);
            this.content = content;
        }
        private String getExtension(){
            return name.substring(name.indexOf(".")+1);
        }

        @Override
        public int getSize() {
            return content.length;
        }

        @Override
        public boolean isDirectory() {
            return false;
        }
        public byte[] getContent(){
            return content;
        }
        public void setContent(byte[] content){
            this.content = content;
        }
        @Override
        public String toString(){
            return this.name;
        }
    }
    
    public class Directory extends Entry{
        List<Entry> entries = new ArrayList();

        public Directory(String name) {
            super(name);
        }
        @Override
        public int getSize() {
            int size=0;
            for (Entry entry: entries){
                size+=entry.getSize();
            }
            return size;
        }

        @Override
        public boolean isDirectory() {
            return true;
        }
        public void addEntry(Entry entry){
            entries.add(entry);
        }
        public List<Entry> getEntries(){
            return this.entries;
        }
    }
    public class SearchParams {
        String extension;
        Integer minSize;
        Integer maxSize;
        String name;
        public SearchParams(){
            
        }
    } 
    public interface Filter{
        List<File> filter(SearchParams params, List<File> files);
    }
    public class ExtensionFilter implements Filter{
        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            return files.stream().filter(file->file.getExtension().equals(params.extension)).collect(toList());
        }
    }
    public class MinSizeFilter implements Filter{
        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            return files.stream().filter(file-> params.minSize<=file.getSize()).collect(toList());
        }
    }
    public class MaxSizeFilter implements Filter{
        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            return files.stream().filter(file-> params.maxSize>=file.getSize()).collect(toList());
        }
    }
    public class NameFilter implements Filter{
        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            return files.stream().filter(file-> params.name.equals(file.getName())).collect(toList());
        }
    }
    
    public class AndFilter implements Filter{
        private Filter[] filters;
        
        public AndFilter(Filter... filters){
            this.filters = filters;
        }

        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            for (Filter filter : filters){
                files = filter.filter(params, files);
            }
            return files;
        }
        
    }
    //https://www.tutorialspoint.com/design_pattern/filter_pattern.htm
    //if any conditions satisfy, return file. e.g. size=2 or name="abc", return file when only size matches
    public class ORFilter implements Filter{
        private Filter[] filters;
        
        public ORFilter(Filter... filters){
            this.filters = filters;
        }

        @Override 
        public List<File> filter(SearchParams params, List<File> files){
            List<File> result_files = new ArrayList();
            List<File> filtered = new ArrayList();
            for (int i=0;i<this.filters.length;i++){
                filtered = this.filters[i].filter(params, files);
                for (File file:filtered){
                    if (!result_files.contains(file)){
                        result_files.add(file);
                    }
                }
            }
            return result_files;
        }
        
    }
}

