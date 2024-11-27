features_1 = ['height_cm','weight_kg', 'body_type','physic','preferred_foot','weak_foot', 
              'pace', 'shooting', 'passing', 'dribbling', 'defending', 'goalkeeping_speed']
       
features_2 = ['goalkeeping_average', 'defense_average', 'attacking_average', 'height_cm','weight_kg', 
              'power_stamina','power_long_shots','power_shot_power','power_strength', 'power_jumping',
              'mentality_aggression', 'mentality_vision', 'mentality_interceptions']

features_3 = ['power_stamina','power_long_shots','power_shot_power','power_strength', 'power_jumping',
               'height_cm','weight_kg',  'shooting', 'pace', 'dribbling', 'attacking_crossing', 'movement_sprint_speed',
              'weak_foot', 'preferred_foot', 'work_rate',
              'mentality_aggression', 'mentality_vision', 'mentality_interceptions', 'defense_average', 'attacking_average']
features_4 = ['power_stamina','height_cm','weight_kg',  'shooting', 'dribbling', 'attacking_crossing', 'preferred_foot', 'work_rate',
              'mentality_aggression',  'defense_average', 'attacking_average', 'goalkeeping_speed']

features_5 = ['overall', 'potential', 'value_eur', 'wage_eur', 'height_cm','weight_kg',
       'nationality_name', 'preferred_foot', 'weak_foot', 'skill_moves',
       'international_reputation', 'work_rate', 'body_type', 'pace',
       'shooting', 'passing', 'dribbling', 'defending', 'physic',
       'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
        'goalkeeping_speed']

features_6 = ['overall', 'potential', 'value_eur', 'wage_eur', 'height_cm','weight_kg',
       'nationality_name', 'preferred_foot',  'skill_moves',
       'international_reputation', 'work_rate', 'body_type', 'pace',
       'shooting', 'passing', 'dribbling', 'defending', 'physic',
       'attacking_crossing', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control','movement_sprint_speed',
       'power_stamina', 'mentality_aggression', 'goalkeeping_speed']
features_7 = ['overall', 'height_cm', 'weight_kg',
       'nationality_name', 'preferred_foot',  'skill_moves',
       'international_reputation', 'work_rate', 'body_type', 'pace',
       'shooting', 'passing', 'dribbling', 'defending', 'physic',
       'attacking_crossing', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control','movement_sprint_speed','power_stamina', 'mentality_aggression', 'goalkeeping_speed']

features_8 = ['defense_average', 'attacking_average', 'mentality_average', 'power_average', 'skills_average', 'movement_average', 'goalkeeping_average']

features_9 = ['defense_average', 'attacking_average', 'mentality_average', 'power_average', 'skills_average', 'movement_average',
              'goalkeeping_speed', 'shooting', 'passing', 'dribbling', 'defending', 'physic','height_cm','weight_kg', 'preferred_foot']

features_10 = ['height_cm',
       'weight_kg', 
        'preferred_foot',
       'weak_foot', 'skill_moves',
       'body_type', 'pace', 'shooting', 'passing', 'dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving']

features_11 = ['overall', 'potential',  'height_cm',
       'weight_kg', 'preferred_foot',
       'weak_foot', 'skill_moves', 'work_rate',
       'body_type', 'pace', 'shooting', 'passing', 'dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes',
       'continent']

features_12 = ['height_cm',
       'weight_kg', 'preferred_foot',
       'weak_foot', 'skill_moves', 'work_rate', 'pace', 'shooting', 'passing', 'dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle']

features_13 = ['overall', 'potential', 'value_eur', 'wage_eur', 'height_cm',
       'weight_kg', 'club_name', 'league_name', 'league_level',
       'nationality_name', 'preferred_foot',
       'weak_foot', 'skill_moves', 'international_reputation', 'work_rate',
       'body_type', 'pace', 'shooting', 'passing', 'dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle', 'age',
       'experience', 'continent']

features_14 = ['overall', 'potential', 'value_eur', 'wage_eur', 'height_cm',
       'weight_kg', 'league_level', 'weak_foot', 'skill_moves',
       'international_reputation', 'pace', 'shooting', 'passing', 'dribbling',
       'defending', 'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed',
       'age', 'experience', 'goalkeeping_average', 'defense_average',
       'attacking_average', 'mentality_average', 'power_average',
       'movement_average', 'skills_average']
