public class Film {
    private String title;
    private String date;
    private String rate;
    
    public Film(String title, String date, String rate) {
        this.title = title;
        this.date = date;
        this.rate = rate;
    }

    @Override
    public String toString() {
        return "Film{" + "title=" + title + ", date=" + date + ", rate=" + rate + '}';
    }
    
    public String getTitle() {
        return title;
    }
    
    
}