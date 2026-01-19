from services.category_service import CategoryService

def main():
    service = CategoryService()

    category_name = input("Enter a category name: ").strip()
    service.create_category(category_name)
    

    categories = service.get_categories()
    for c in categories:
        print(c)

if __name__ == "__main__":
    main()
