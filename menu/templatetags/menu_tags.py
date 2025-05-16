from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    try:
        menu_items = MenuItem.objects.filter(
            menu__name=menu_name).select_related('parent')
        menu_dict = {}
        menu_tree = []

        for menu_item in menu_items:
            menu_dict[menu_item.id] = {
                'menu_item': menu_item,
                'children': [],
                'is_active': menu_item.url == current_path,
                'should_expand': False
            }
        for obj in menu_dict.values():
            parent_id = obj['menu_item'].parent_id
            if parent_id is None:
                menu_tree.append(obj)
                if obj['is_active']:
                    obj['should_expand'] = True
            else:
                menu_dict[parent_id]['children'].append(obj)
                if obj['is_active']:
                    obj['should_expand'] = True
                    while parent_id is not None:
                        menu_dict[parent_id]['should_expand'] = True
                        parent_id = menu_dict[parent_id]['menu_item'].parent_id

        return {'menu_tree': menu_tree}
    except Exception as e:
        print(e)
        return {'menu_tree': []}
