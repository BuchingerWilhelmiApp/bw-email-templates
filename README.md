# Email templates

> Static HTML templates for emails that are sent out by Buchinger Wilhelmi everytime a visit registration form is completed and sent


## Styling

There are two types of files, the template and the compiled template with the inline styles marked with  at the end.

The templates can be styled with classes within the style tags, when the template is ready it must still be compiled with the following tool:

#### https://putsmail.com/inliner

You can also create an account and test the template on different email clients:

#### https://putsmail.com/

# Backend

These templates are used by the bwcontactform-backend to create emails. 
Placeholders in brackets [] are used to replace values with data submitted by the frontend. The guest-mail features curled brackets {} that are replaced by different language versions of that keyword, done by the bwcontactform-backend as well. Check out the backend repo for further instructions: https://github.com/BuchingerWilhelmiApp/bw-contactformbackend
