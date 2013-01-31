properties = {
    'publishing_scope_value': { 
        'name': 'Scope',
        'group': 'publishing_scope',
        'description': '',
        'data' : 'schedule.find("publishing").find("scope").get("value")',
        'type': 'text'
        },
    'publishing_scope_narrative': 
        {
        'name': 'Scope narrative',
        'group': 'publishing_scope',
        'data' : 'schedule.find("publishing").find("scope").find("narrative").text',
        'type': 'text'
        },
    'publishing_timetable_date_initial': 
        {
        'name': 'Initial publication date',
        'group': 'publishing_timetable',
        'data' : 'schedule.find("publishing").find("publication-timetable").get("date-initial")',
        'type': 'text'
        },
    'publishing_timetable_narrative': 
        {
        'name': 'Timetable narrative',
        'group': 'publishing_timetable',
        'data' : 'schedule.find("publishing").find("publication-timetable").find("narrative").text',
        'type': 'text'
        },
    'publishing_frequency_frequency':
        {
        'name': 'Frequency',
        'group': 'publishing_frequency',
        'data' : 'schedule.find("publishing").find("publication-frequency").get("frequency")',
        'type': 'code',
        'code': 'frequency'
        },
    'publishing_frequency_timeliness':
        {
        'name': 'Timeliness',
        'group': 'publishing_frequency',
        'data' : 'schedule.find("publishing").find("publication-frequency").get("timeliness")',
        'type': 'code',
        'code': 'timeliness'
        },
    'publishing_frequency_narrative':
        { 
        'name': 'Frequency narrative',
        'group': 'publishing_frequency',
        'data' : 'schedule.find("publishing").find("publication-frequency").find("narrative").text',
        'type': 'text'
        },
    'publishing_lifecycle_point':
        { 
        'name': 'Lifecycle',
        'group': 'publishing_lifecycle',
        'data' : 'schedule.find("publishing").find("publication-lifecycle").get("point")',
        'type': 'code',
        'code': 'point'
        },
    'publishing_lifecycle_narrative':
        { 
        'name': 'Lifecycle narrative',
        'group': 'publishing_lifecycle',
        'data' : 'schedule.find("publishing").find("publication-lifecycle").find("narrative").text',
        'type': 'text'
        },
    'publishing_data_quality_quality':
        { 
        'name': 'Data quality',
        'group': 'publishing_data_quality',
        'data' : 'schedule.find("publishing").find("data-quality").get("quality")',
        'type': 'code',
        'code': 'quality'
        },
    'publishing_data_quality_narrative':
        { 
        'name': 'Data quality narrative',
        'group': 'publishing_data_quality',
        'data' : 'schedule.find("publishing").find("data-quality").find("narrative").text',
        'type': 'text'
        },
    'publishing_approach_resource':
        { 
        'name': 'Publishing approach',
        'group': 'publishing_approach',
        'data' : 'schedule.find("publishing").find("approach").get("resource")',
        'type': 'code',
        'code': 'resource'
        },
    'publishing_approach_narrative':
        { 
        'name': 'Publishing approach narrative',
        'group': 'publishing_approach',
        'data' : 'schedule.find("publishing").find("approach").find("narrative").text',
        'type': 'text'
        },
    'publishing_notes':
        { 
        'name': 'Notes',
        'group': 'publishing_notes',
        'data' : 'schedule.find("publishing").find("notes").find("narrative").text',
        'type': 'text'
        },
    'publishing_thresholds':
        { 
        'name': 'Threshold',
        'group': 'publishing_thresholds',
        'data' : 'schedule.find("publishing").find("thresholds").find("narrative").text',
        'type': 'text'
        },
    'publishing_exclusions':
        { 
        'name': 'Exclusions',
        'group': 'publishing_exclusions',
        'data' : 'schedule.find("publishing").find("exclusions").find("narrative").text',
        'type': 'text'
        },
    'publishing_constraints':
        {
        'name': 'Constraints',
        'group': 'publishing_constraints',
        'data' : 'schedule.find("publishing").find("constraints-other").find("narrative").text',
        'type': 'text'
        },
    'publishing_license':
        { 
        'name': 'License',
        'group': 'publishing_license',
        'data' : 'schedule.find("publishing").find("license").get("license")',
        'type': 'code',
        'code': 'license'
        },
    'publishing_license_narrative':
        { 
        'name': 'License narrative',
        'group': 'publishing_license',
        'data' : 'schedule.find("publishing").find("license").find("narrative").text',
        'type': 'text'
        },
    'publishing_multilevel':
        { 
        'name': 'Multilevel publication',
        'group': 'publishing_multilevel',
        'data' : 'schedule.find("publishing").find("activity-multilevel").get("yesno")',
        'type': 'code',
        'code': 'yesno'
        },
    'publishing_multilevel_narrative':
        { 
        'name': 'Multilevel publication narrative',
        'group': 'publishing_multilevel',
        'data' : 'schedule.find("publishing").find("activity-multilevel").find("narrative").text',
        'type': 'text'
        },
    'publishing_segmentation':
        { 
        'name': 'Segmentation',
        'group': 'publishing_segmentation',
        'data' : 'schedule.find("publishing").find("segmentation").get("segmentation")',
        'type': 'code',
        'code': 'segmentation'
        },
    'publishing_segmentation_narrative':
        { 
        'name': 'Segmentation narrative',
        'group': 'publishing_segmentation',
        'data' : 'schedule.find("publishing").find("segmentation").find("narrative").text',
        'type': 'text'
        },
    'publishing_user_interface_status':
        { 
        'name': 'User interface',
        'group': 'publishing_user_interface',
        'data' : 'schedule.find("publishing").find("user-interface").get("status")',
        'type': 'code',
        'code': 'status'
        },
    'publishing_user_interface_narrative':
        {
        'name': 'User interface narrative',
        'group': 'publishing_user_interface',
        'data' : 'schedule.find("publishing").find("segmentation").find("narrative").text',
        'type': 'text'
    }
}
status = {    'fc': 'Fully compliant',
              'fp': 'Future publication',
              'pc': 'Partially compliant',
              'up': 'Unable to publish',
              'uc': 'Under consideration',
              'na': 'Not applicable'
         }

codes = {   
    # Data quality
    'quality': {   'u': 'Unverified', 'v': 'Verified'},
    # Frequency
    'frequency': {   'a': 'Annually',
                     'b': 'Bi-annually',
                     'f': 'Fortnightly',
                     'm': 'Monthly',
                     'o': 'Other',
                     'q': 'Quarterly',
                     'r': 'Real time',
                     'w': 'Weekly'},
    # License type
    'license': {    'a': 'Attribution-only',
                    'o': 'Other (non-compliant)',
                    'p': 'Public domain'},
    # Lifecyle
    'point': {   'i': 'Implementation',
                 'o': 'Other',
                 'p': 'Pipeline/identification'},
    # Multi-level reporting
    'yesno': {   'n': 'No', 'y': 'Yes'},
    # Multi-level type
    'UNUSED': { 'b': 'Both',
                'h': 'Hierarchy',
                'r': 'Related activities'},
    # Segmentation
    'segmentation': {   'b': 'By country / region',
                        'o': 'Other',
                        's': 'Single file'},
    # Staff resource
    'UNUSED2': {  'a': 'Ad hoc',
                  'd': 'Dedicated resource',
                  'o': 'Other',
                  'w': 'Working group'},
    # System resource
    'resource': {  'd': 'Direct feed from internal systems',
                   'e': 'Excel spreadsheet conversion',
                   'm': 'Manual capture through an online tool (web entry platform)',
                   'o': 'Other'},
    # Timeliness
    'timeliness': {   '1m': '1 month in arrears',
                      '1q': '1 quarter in arrears',
                      '1w': '1 week in arrears',
                      '2m': '2 months in arrears',
                      '2w': '2 weeks in arrears',
                      'gt': '> 1 quarter in arrears',
                      'o': 'Other',
                      'r': 'Real time'},
    # User interface
    'status': {   'i': 'In development',
                  'n': 'No',
                  'u': 'Under consideration',
                  'y': 'Yes'}}
change_reasons = {
    'no_date': 'No date provided',
    'initial_date': 'Initial date later',
    'parse_error': 'Not parsed properly',
    'typo': 'Fix typo',
    'missing': 'Information missing'
}
