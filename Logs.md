### Version 0.0
- Initiated Django Project.
- Created app nexus.
- Created urls.py for nexus.
- Created template for Home Page at ./nexus/templates/home.html.

### Version 0.1
- Created Navbar for all.
- Connected custom CSS files through static.
- Created base layout for all pages at ./nexus/templates/base.html.

### Version 0.2
- Changed the inbuilt User profile at ./nexus/admin.py.
- Created profile model and connected attributes at ./nexus/models.py.
- Automated profile creations for Profile model.

### Version 0.3
- Follow and Unfollow system initiated.
- Profile view showcasing accounts thay follow and unfollow at ./nexus/views.py.
- View user profile hidden until authenticated.
- Error banners added through ./nexus/templates/base.html.
- Each individual profile page for users.
- Bug for Followers and Following not shown solved (rendering problem).

### Version 0.4
- Tweet system implemented (called Nex p:Nux).
- Nux model defined at ./nexus/model.py and implemented by ./nexus/views.py.

### Version 0.5
- Nex postings from forms initiated at ./nexus/forms.py.
- View system for Nex page changed to use on validation done at ./nexus/views.py.

### Version 0.6
- Authentication system for users login and logout.
- Separate login page template at ./nexus/templates/login.html.
- Authentication system initiated at ./nexus/views.py.

### Version 0.7
- Authentication system for registration of new users.
- Separate registration template at ./nexus/templates/register.html.
- Authentication system done at ./nexus/views.py.
- Registration form system done at ./nexus/forms.py.
- Update profile system with template at ./nexus/templates/update_user.html.

### Version 0.8
- Picture handling option enabled from ./project/settings.py.
- Media url added for media at ./project/urls.py.
- Profile Picture attribute creation at ./nexus/models.py.
- Profile pic upload form creation at ./nexus/forms.py.
- Profile pic view option at profile page, profile_list page and home page.
- Foreign key reference for home page for the profile pic.
- New media folder where profile pictures are stored.
- Logic for profile viewing at ./nexus/views.py.

### Version 0.9
- Like and unlike system for Nex creation.
- Likes system model designed at ./nexus/models.py.
- Like rendering system created via views at ./nexus/views.py and ./nexus/urls.py.
- Like system render working tests.
- Like texts reflected using heart symbols.

### Version 0.10
- Viewing option for individual Nex.
- Separate template creation at ./nexus/templates/show_nex.py.

### Version 0.11
- Profile bio and other social link models created at ./nexus/models.py.
- Displayed at profile page of user.
- Profile icon button for profile page navigation done in ./nexus/templates/navbar.html.
- Follow and Unfollow system from profile page system made.
- New view system and url at ./nexus/views.py and ./nexus/urls.py.
- Form model for profile bio and likes at ./nexus/forms.py.

### Version 0.12
- Separate followers and following viewing page created.
- Followers and Following views created at ./nexus/views.py.
- Following and Unfollowing from specific pages option enabled as well.
