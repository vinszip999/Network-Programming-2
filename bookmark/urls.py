from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, \
    BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # bookmark:list
    # path('list/', BookmarkListView.as_view(), name='list'),  # bookmark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),  # bookmark:add
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),  # bookmark:detail
    path('edit/<int:pk>/', BookmarkUpdateView.as_view(), name='edit'),  # bookmark:edit
    # 특정 북마크를 삭제할 것이기 때문에 그것을 가리킬 pk가 있어야 한다. 그러므로, delete도 pk가 있어야 한다.
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),  # bookmark:delete
]
