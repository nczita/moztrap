'''
Created on Feb 9, 2011

@author: camerondawson
'''
from features.models import TagModel, CompanyModel
from features.tcm_data_helper import get_stored_or_store_field
from features.tcm_request_helper import do_post, do_delete
from lettuce import step, world


'''
######################################################################

                     TAG STEPS

######################################################################
'''

@step(u'create a new tag with (that tag|tag "(.*)")')
def create_tag_with_name(step, stored, tag):
    tag = get_stored_or_store_field("tag", "tag", stored, tag)

    post_payload = {"companyId": CompanyModel().get_seed_resid()[0],
                    "tag": tag
                   }

    do_post(world.path_tags,
            post_payload)



@step(u'tag with (that tag|tag "(.*)") (exists|does not exist)')
def check_tag_foo_existence(step, stored, tag, existence):
    tagModel = TagModel()
    tag = tagModel.get_stored_or_store_tag(stored, tag)
    tagModel.verify_existence_on_root(existence = existence,
                                      params = {"tag": tag})


@step(u'delete the tag with (that tag|tag "(.*)")')
def delete_tag_with_tag_foo(step, stored, tag):
    tag = get_stored_or_store_field("tag", "tag", stored, tag)

    tag_id, version = TagModel().get_resid(tag)

    do_delete(world.path_tags + str(tag_id),
              {"originalVersionId": version})

