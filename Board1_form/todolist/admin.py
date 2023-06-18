from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "user", "comments_count", "tags_list"]
    search_fields = ["title"]
    list_filter = ["user"]

    date_hierarchy = "created"
    list_select_related = ["user"]
    actions = ["add_tag_python"]

    @admin.action(description="Добавить тег python")
    def add_tag_python(self, form, queryset):
        tag, _ = Tag.objects.get_or_create(name="python")
        for obj in queryset:
            obj.tags.add(tag)

    @admin.display(description="Кол-во комментариев")
    def comments_count(self, obj: Post):
        return obj.comments_count

    @admin.display(description="Теги", boolean=True)
    def tags_list(self, obj: Post):
        return (obj.tags.count()>0)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "posts_list"]

    @admin.display(description="Posts")
    def posts_list(self, obj: Tag):
        list_ = list(obj.posts.values_list("title", flat=True))
        return list_





