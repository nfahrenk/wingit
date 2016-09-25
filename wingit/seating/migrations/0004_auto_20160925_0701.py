# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0002_auto_20160925_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='industry',
        ),
        migrations.AddField(
            model_name='person',
            name='ind',
            field=models.IntegerField(default=47, choices=[(47, b'Accounting'), (94, b'Airlines/Aviation'), (120, b'Alternative Dispute Resolution'), (125, b'Alternative Medicine'), (127, b'Animation'), (19, b'Apparel & Fashion'), (50, b'Architecture & Planning'), (111, b'Arts and Crafts'), (53, b'Automotive'), (52, b'Aviation & Aerospace'), (41, b'Banking'), (12, b'Biotechnology'), (36, b'Broadcast Media'), (49, b'Building Materials'), (138, b'Business Supplies and Equipment'), (129, b'Capital Markets'), (54, b'Chemicals'), (90, b'Civic & Social Organization'), (51, b'Civil Engineering'), (128, b'Commercial Real Estate'), (118, b'Computer & Network Security'), (109, b'Computer Games'), (3, b'Computer Hardware'), (5, b'Computer Networking'), (4, b'Computer Software'), (48, b'Construction'), (24, b'Consumer Electronics'), (25, b'Consumer Goods'), (91, b'Consumer Services'), (18, b'Cosmetics'), (65, b'Dairy'), (1, b'Defense & Space'), (99, b'Design'), (69, b'Education Management'), (132, b'E-Learning'), (112, b'Electrical/Electronic Manufacturing'), (28, b'Entertainment'), (86, b'Environmental Services'), (110, b'Events Services'), (76, b'Executive Office'), (122, b'Facilities Services'), (63, b'Farming'), (43, b'Financial Services'), (38, b'Fine Art'), (66, b'Fishery'), (34, b'Food & Beverages'), (23, b'Food Production'), (101, b'Fund-Raising'), (26, b'Furniture'), (29, b'Gambling & Casinos'), (145, b'Glass, Ceramics & Concrete'), (75, b'Government Administration'), (148, b'Government Relations'), (140, b'Graphic Design'), (124, b'Health, Wellness and Fitness'), (68, b'Higher Education'), (14, b'Hospital & Health Care'), (31, b'Hospitality'), (137, b'Human Resources'), (134, b'Import and Export'), (88, b'Individual & Family Services'), (147, b'Industrial Automation'), (84, b'Information Services'), (96, b'Information Technology and Services'), (42, b'Insurance'), (74, b'International Affairs'), (141, b'International Trade and Development'), (6, b'Internet'), (45, b'Investment Banking'), (46, b'Investment Management'), (73, b'Judiciary'), (77, b'Law Enforcement'), (9, b'Law Practice'), (10, b'Legal Services'), (72, b'Legislative Office'), (30, b'Leisure, Travel & Tourism'), (85, b'Libraries'), (116, b'Logistics and Supply Chain'), (143, b'Luxury Goods & Jewelry'), (55, b'Machinery'), (11, b'Management Consulting'), (95, b'Maritime'), (97, b'Market Research'), (80, b'Marketing and Advertising'), (135, b'Mechanical or Industrial Engineering'), (126, b'Media Production'), (17, b'Medical Devices'), (13, b'Medical Practice'), (139, b'Mental Health Care'), (71, b'Military'), (56, b'Mining & Metals'), (35, b'Motion Pictures and Film'), (37, b'Museums and Institutions'), (115, b'Music'), (114, b'Nanotechnology'), (81, b'Newspapers'), (100, b'Organization Management'), (57, b'Oil & Energy'), (113, b'Online Media'), (123, b'Outsourcing/Offshoring'), (87, b'Package/Freight Delivery'), (146, b'Packaging and Containers'), (61, b'Paper & Forest Products'), (39, b'Performing Arts'), (15, b'Pharmaceuticals'), (131, b'Philanthropy'), (136, b'Photography'), (117, b'Plastics'), (107, b'Political Organization'), (67, b'Primary/Secondary Education'), (83, b'Printing'), (105, b'Professional Training & Coaching'), (102, b'Program Development'), (79, b'Public Policy'), (98, b'Public Relations and Communications'), (78, b'Public Safety'), (82, b'Publishing'), (62, b'Railroad Manufacture'), (64, b'Ranching'), (44, b'Real Estate'), (40, b'Recreational Facilities and Services'), (89, b'Religious Institutions'), (144, b'Renewables & Environment'), (70, b'Research'), (32, b'Restaurants'), (27, b'Retail'), (121, b'Security and Investigations'), (7, b'Semiconductors'), (58, b'Shipbuilding'), (20, b'Sporting Goods'), (33, b'Sports'), (104, b'Staffing and Recruiting'), (22, b'Supermarkets'), (8, b'Telecommunications'), (60, b'Textiles'), (130, b'Think Tanks'), (21, b'Tobacco'), (108, b'Translation and Localization'), (92, b'Transportation/Trucking/Railroad'), (59, b'Utilities'), (106, b'Venture Capital & Private Equity'), (16, b'Veterinary'), (93, b'Warehousing'), (133, b'Wholesale'), (142, b'Wine and Spirits'), (119, b'Wireless'), (103, b'Writing and Editing')]),
            preserve_default=False,
        ),
    ]
