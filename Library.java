class Book{
    String name;
    String author;
    int publishedYear;

    Book(String name, String author, int publishedYear){
        this.name = name;
        this.author = author;
        this.publishedYear = publishedYear;
    }

    public String getInfo(){
        return "Title: " + this.name + "\nAuthor: " + this.author + " \nPublished Year: " + this.publishedYear;
    }

    public void getDetails(){
        System.out.println(this.getInfo());
    }
}


class PrintedBook extends Book{
    int NumberOfPages;
    String publisher;
    int price;

    PrintedBook(String name, String author, int publishedYear, int NumberOfPages, String publisher){
        super(name, author, publishedYear);
        this.NumberOfPages = NumberOfPages;
        this.publisher = publisher;
        this.price = NumberOfPages * 5;
    }

    @Override
    public String getInfo(){
        return "Printed Book info \n" + super.getInfo() + " \nNumber of pages: " + this.NumberOfPages + " \nPublisher: " + this.publisher;
    }

    @Override
    public void getDetails(){
        System.out.println(this.getInfo());
    }

    public void bookType(){
        System.out.println("This is a printed book.");
    }

    public void printingBook(){
        System.out.println("Printing the book...");
        System.out.println(this.getInfo());
    }

    public void getPrice(){
        System.out.println(this.price);
    }
}

class EBook extends Book{
    double SizeOfBook;
    String fileFormat;
    double price;
    EBook(String name, String author, int publishedYear, double SizeOfBook, String fileFormat){
        super(name, author, publishedYear);
        this.SizeOfBook = SizeOfBook;
        this.fileFormat = fileFormat;
        this.price = SizeOfBook * 10;
    }

    @Override
    public String getInfo(){
        return "Ebook info\n" + super.getInfo() + "\nSize of book: " + this.SizeOfBook + "MB" + "\nFile format: " + this.fileFormat;
    }

    @Override
    public void getDetails(){
        System.out.println(this.getInfo());
    }

    public void bookType(){
        System.out.println("This is an e-book.");
    }

    public void getPrice(){
        System.out.println(this.price);
    }
}


class Library{
    public static void main(String[] args) {
        Book book1 = new Book("Хроники Кыргызстана", "Бакыт Алиев", 2018);
        book1.getDetails();

        PrintedBook book2 = new PrintedBook("Тень гор", "Толгонай Ашимова", 1985, 320, "Авторы Центральной Азии");
        book2.getDetails();
        book2.bookType();
        book2.getPrice();
        book2.printingBook();

        EBook book3 = new EBook("Евгений Онегин", "Пушкин Александр", 1850, 10.5, "epub");
        book3.getDetails();
        book3.bookType();
        book3.getPrice();
    }
}
