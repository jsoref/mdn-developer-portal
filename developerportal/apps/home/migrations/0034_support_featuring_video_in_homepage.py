# Generated by Django 2.2.7 on 2019-11-10 21:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("home", "0033_rephrase_articles_as_posts")]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="featured",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "post",
                        wagtail.core.blocks.PageChooserBlock(
                            page_type=[
                                "articles.Article",
                                "externalcontent.ExternalArticle",
                            ]
                        ),
                    ),
                    (
                        "external_page",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("url", wagtail.core.blocks.URLBlock()),
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "description",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ]
                        ),
                    ),
                    (
                        "video",
                        wagtail.core.blocks.PageChooserBlock(
                            page_type=["videos.Video"]
                        ),
                    ),
                ],
                blank=True,
                help_text="Optional space for featured posts, videos or links, min. 2, max. 5. Note that External Video is NOT allowed here.",
                null=True,
            ),
        )
    ]
